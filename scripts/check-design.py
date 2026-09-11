#!/usr/bin/env python3
"""
check-design.py — enforce the design.md rules that a script can actually settle.

Why this exists, and it is the whole point:

    design.md states the rules. A controlled test on 2026-09-11 ran twelve fresh
    agents — six with design.md and ux.md present, six with them deleted — on
    tasks that were traps those files specifically forbid. Five of six task pairs
    tied. One treatment agent put an emoji in the markup while holding the file
    that bans emoji. Another built a confirmation dialog while holding the section
    that says discard must never be confirmed.

    The content was fine. It was not in the execution path.

    A rule in a document is a hope. A rule a script checks at the moment of the
    decision is a rule. This script is the second kind. It prints the rule and the
    fix, not a box id, because the output is the only place the content lands.

What this does NOT do, stated plainly so nobody mistakes a green run for an audit:
it cannot see rendered output, so it cannot check target size, focus-ring
visibility in practice, keyboard order, or whether a colour pair is legible in
context. It resolves backgrounds by a documented assumption (see ASSUMPTION
below) and reports UNRESOLVED rather than guessing when it cannot tell. An
UNRESOLVED is a question for a person, not a pass.

ASSUMPTION: a rule's background is its own `background`/`background-color` if it
declares one, otherwise the page ground `--paper`. This holds for this prototype
because exactly one element (.fidelity-banner) declares a dark ground. If that
stops being true, this assumption must be revisited — it is not a general truth.

Exit codes, distinct from the other scripts on purpose:
    0  no violations
    6  at least one violation
    7  no violations, but unresolved pairs a human must settle
"""

import re
import sys
import os

# ---------------------------------------------------------------- palette
PALETTE = {
    "vermillion": "#D8472B", "ultramarine": "#1F3C96", "ochre": "#C99A2E",
    "violet": "#5B3A7E", "green-earth": "#5E7A3F", "cadmium": "#E8B93A",
    "ink": "#1a1612", "paper": "#efe7d6", "card": "#f7f0df",
    "line": "#1a1612",  # --line: var(--ink)
}


def _lin(c):
    c = c / 255
    return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4


def luminance(hexv):
    h = hexv.lstrip("#")
    if len(h) == 3:
        h = "".join(ch * 2 for ch in h)
    r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    return 0.2126 * _lin(r) + 0.7152 * _lin(g) + 0.0722 * _lin(b)


def contrast(a, b):
    la, lb = luminance(a), luminance(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)


# ---------------------------------------------------------------- findings
violations = []
unresolved = []
passes = []
moot = []


def fail(rule, where, detail, fix):
    violations.append((rule, where, detail, fix))


def ask(rule, where, detail, question):
    unresolved.append((rule, where, detail, question))


def ok(rule, detail):
    passes.append((rule, detail))


# ---------------------------------------------------------------- input
def load(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def style_blocks(src):
    css = "\n".join(re.findall(r"<style[^>]*>(.*?)</style>", src, re.S))
    # Strip CSS comments FIRST. The naive rule regex treats everything between
    # `}` and `{` as the selector, so a section comment gets glued onto the front
    # of the next selector: `.fidelity-banner` was keyed as
    # `/* ===== Fidelity banner ===== */ .fidelity-banner` and never matched an
    # ancestor lookup. That silently mis-keyed 24 of the background entries and
    # produced a confident false positive.
    return re.sub(r"/\*.*?\*/", "", css, flags=re.S)


RULE_RE = re.compile(r"([^{}]+)\{([^{}]*)\}", re.S)


def rules(css):
    """Yield (selector, declarations-dict, raw) for each CSS rule."""
    for m in RULE_RE.finditer(css):
        sel = " ".join(m.group(1).split())
        if sel.startswith("@") or not sel:
            continue
        decls = {}
        for part in m.group(2).split(";"):
            if ":" not in part:
                continue
            k, _, v = part.partition(":")
            decls[k.strip().lower()] = v.strip()
        yield sel, decls, m.group(2)


def token_of(value):
    """Return the palette key for `var(--x)` / a literal hex, else None."""
    if value is None:
        return None
    m = re.search(r"var\(\s*--([a-z-]+)\s*\)", value)
    if m and m.group(1) in PALETTE:
        return m.group(1)
    m = re.search(r"(#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3})\b", value)
    if m:
        for k, v in PALETTE.items():
            if v.lower() == m.group(1).lower():
                return k
    return None


def px(value):
    if not value:
        return None
    m = re.search(r"([\d.]+)px", value)
    return float(m.group(1)) if m else None


def is_bold(decls):
    w = decls.get("font-weight", "")
    return "bold" in w or (w.strip().isdigit() and int(w.strip()) >= 700)


# ================================================================ checks
def _background_index(css_rules):
    """selector -> background token, for rules that declare one."""
    idx = {}
    for sel, d, _ in css_rules:
        bg = token_of(d.get("background") or d.get("background-color"))
        if bg:
            for one in sel.split(","):
                idx[one.strip()] = bg
    return idx


def resolve_background(sel, d, bg_index):
    """Own background, else the nearest declared ancestor's, else the page ground.

    The ancestor step is not optional. `.fidelity-banner strong` sets a cadmium
    colour and no background, but `.fidelity-banner` sets `background:
    var(--ultramarine)`, where cadmium is 5.33:1 and passes. Assuming the page
    ground for every rule without its own background reported that as a 1.49:1
    violation — a false positive, and a linter that cries wolf gets switched off.
    Returns (token, how) where `how` is 'own' | 'inherited from X' | 'assumed'.
    """
    own = token_of(d.get("background") or d.get("background-color"))
    if own:
        return own, "own"

    # walk the descendant chain right-to-left: ".a .b strong" -> ".a .b", ".a"
    parts = sel.split(",")[0].strip().split()
    for i in range(len(parts) - 1, 0, -1):
        ancestor = " ".join(parts[:i])
        if ancestor in bg_index:
            return bg_index[ancestor], f"inherited from {ancestor}"
        # also try the bare last token of the ancestor (".sw-stat .num" -> ".sw-stat")
        if parts[i - 1] in bg_index:
            return bg_index[parts[i - 1]], f"inherited from {parts[i - 1]}"

    return "paper", "assumed"


def check_contrast(css_rules):
    """CLR-01, CLR-02 and WCAG 1.4.3 — the rules with numbers behind them."""
    bg_index = _background_index(css_rules)
    for sel, d, _ in css_rules:
        fg = token_of(d.get("color"))
        if not fg:
            continue
        bg, how = resolve_background(sel, d, bg_index)
        assumed = how == "assumed"

        ratio = contrast(PALETTE[fg], PALETTE[bg])
        size = px(d.get("font-size"))
        bold = is_bold(d)
        large = size is not None and (size >= 24 or (size >= 18.66 and bold))
        need = 3.0 if large else 4.5

        where = f"{sel} {{ color: {fg} on {bg}{'' if how=='own' else ' (' + how + ')'} }}"

        if ratio >= 4.5:
            continue  # passes at any size

        if size is None:
            ask("CLR-02 / WCAG 1.4.3", where,
                f"{ratio:.2f}:1 — below the 4.5:1 minimum for normal text, and this "
                f"rule sets no font-size, so the size is inherited and cannot be "
                f"resolved from the stylesheet.",
                "What size does this text actually render at? If under 24px "
                "(or under 18.66px bold) it is a 1.4.3 failure.")
            continue

        if ratio < need:
            if fg in ("ochre", "cadmium"):
                rule = "CLR-01"
                fixtxt = (f"--{fg} may never carry text on a light ground. Use it as a "
                          f"fill or border with --ink text on top, or switch the text to "
                          f"--ink / --ultramarine / --violet (CLR-03).")
            else:
                rule = "CLR-02"
                fixtxt = (f"--{fg} clears 3:1 but not 4.5:1, so it is headings >=24px "
                          f"(or >=18.66px bold), icons and borders only — not {size:g}px "
                          f"body text. Use --ink, or raise the size past 24px.")
            fail(f"{rule} / WCAG 1.4.3", where,
                 f"{ratio:.2f}:1 at {size:g}px{' bold' if bold else ''} — needs {need}:1.",
                 fixtxt)


def check_shadows(css):
    """SHD-01 hard and opaque · SHD-02 down-right, equal, multiple of 3."""
    found = re.findall(r"box-shadow\s*:\s*([^;}]+)", css)
    seen = set()
    for raw in found:
        v = raw.strip()
        if v in seen or v == "none":
            continue
        seen.add(v)

        if "rgba" in v or "hsla" in v:
            fail("SHD-01", f"box-shadow: {v}",
                 "The shadow is translucent.",
                 "Use a fully opaque `6px 6px 0 var(--ink)`. A translucent shadow "
                 "reads as Material and breaks the Bauhaus register.")
            continue

        nums = re.findall(r"(-?[\d.]+)px", v)
        if len(nums) >= 3 and float(nums[2]) != 0:
            fail("SHD-01", f"box-shadow: {v}",
                 f"Blur radius is {nums[2]}px, not 0.",
                 "The shadow is hard. Third value must be 0.")
            continue

        if len(nums) >= 2:
            x, y = float(nums[0]), float(nums[1])
            if x < 0 or y < 0:
                fail("SHD-02", f"box-shadow: {v}",
                     f"Offset ({x:g}, {y:g}) is not down-and-right.",
                     "One light source, never reconsidered per component. Offset is "
                     "always positive on both axes.")
            elif x != y:
                fail("SHD-02", f"box-shadow: {v}",
                     f"Offset ({x:g}, {y:g}) is not equal on both axes.",
                     "Offset is always equal on both axes.")
            elif x % 3 != 0:
                fail("SHD-02", f"box-shadow: {v}",
                     f"Offset {x:g}px is not a multiple of 3.",
                     "Use 3px, 6px or the 2px pressed token --shadow-pressed.")


def check_radius(css):
    hits = re.findall(r"border-radius\s*:\s*([^;}]+)", css)
    bad = [h.strip() for h in hits if not re.fullmatch(r"0[a-z%]*", h.strip())]
    if bad:
        fail("SHD-03", f"border-radius: {', '.join(sorted(set(bad)))}",
             f"{len(bad)} non-zero border-radius declaration(s).",
             "border-radius is 0 everywhere, no exceptions — including avatars, "
             "badges and inputs.")
    else:
        ok("SHD-03", "no non-zero border-radius")


def check_emoji(src):
    ranges = [
        (0x1F300, 0x1FAFF), (0x1F000, 0x1F2FF), (0x2600, 0x27BF),
        (0x2190, 0x21FF), (0xFE0F, 0xFE0F), (0x2B00, 0x2BFF),
    ]
    allowed = {"·", "—", "–", "→", "✓", "×"}  # typographic marks in use
    hits = {}
    for ch in src:
        cp = ord(ch)
        if ch in allowed:
            continue
        if any(lo <= cp <= hi for lo, hi in ranges):
            hits[ch] = hits.get(ch, 0) + 1
    if hits:
        listing = ", ".join(f"{c!r} ×{n} (U+{ord(c):04X})" for c, n in hits.items())
        fail("SHD-06", listing,
             "Emoji or dingbat characters present.",
             "No emoji, anywhere. Shapes, rules and text labels do that work. "
             "For a warning, use a --cadmium fill chip with --ink text.")
    else:
        ok("SHD-06", "no emoji or dingbats")


def check_focus(css):
    if not re.search(r":focus(-visible)?\b", css):
        fail("ds:3 state canon / WCAG 2.4.7", "no :focus or :focus-visible rule",
             "Not one focus style is defined, so the browser default is doing this "
             "job by accident.",
             "Define `:focus-visible { outline: 3px solid var(--ultramarine); "
             "outline-offset: 2px; }` — 7.96:1 on paper, clears the 3:1 non-text "
             "minimum with room.")
    else:
        ok("ds:3 focus", "a focus style is defined")


def check_reduced_motion(css):
    has_motion = bool(re.search(r"\b(transition|animation)\s*:", css))
    has_guard = "prefers-reduced-motion" in css
    if has_motion and not has_guard:
        fail("ds:1.5", "no prefers-reduced-motion block",
             "Animation is declared with no reduced-motion guard.",
             "Add `@media (prefers-reduced-motion: reduce)` that REMOVES transform "
             "and opacity animation — not merely shortens it.")
    elif not has_motion:
        moot.append(("ds:1.5",
                     "no transition or animation is declared anywhere, so the "
                     "reduced-motion rule has nothing to guard. Not a pass — the rule "
                     "is moot, and becomes live the moment any motion is added."))
    else:
        ok("ds:1.5", "prefers-reduced-motion guard present")


def check_hardcoded_hex(src, css):
    """G3-12 — palette defined once in :root, no ad-hoc hex elsewhere."""
    root = re.search(r":root\s*\{[^}]*\}", css, re.S)
    root_span = root.span() if root else (-1, -1)
    body = re.sub(r"<style[^>]*>.*?</style>", "", src, flags=re.S)

    offenders = {}
    # inside CSS but outside :root
    for m in re.finditer(r"(#[0-9a-fA-F]{6})\b", css):
        if root_span[0] <= m.start() <= root_span[1]:
            continue
        offenders.setdefault(m.group(1), 0)
        offenders[m.group(1)] += 1
    # inside markup (SVG stroke/fill attributes etc.)
    for m in re.finditer(r"(#[0-9a-fA-F]{6})\b", body):
        offenders.setdefault(m.group(1), 0)
        offenders[m.group(1)] += 1

    if offenders:
        listing = ", ".join(f"{h} ×{n}" for h, n in sorted(offenders.items()))
        named = [f"{h} is --{k}" for h in offenders
                 for k, v in PALETTE.items() if v.lower() == h.lower()]
        fail("G3-12 / ds:1.1", listing,
             f"{sum(offenders.values())} hardcoded hex value(s) outside the :root "
             f"token block" + (f" — {'; '.join(sorted(set(named)))}." if named else "."),
             "Components reference tokens, never raw values. That is what lets the "
             "palette change without touching a component. Replace with var(--token); "
             "in SVG attributes use `stroke=\"currentColor\"` or a CSS rule.")
    else:
        ok("G3-12", "no hardcoded hex outside :root")


def check_doodle_alt(src):
    """UXI-13 / G3-20 — every doodle carries a text alternative."""
    svgs = re.findall(r"<svg\b[^>]*>", src)
    if not svgs:
        return
    missing = [s for s in svgs
               if "aria-label" not in s and "aria-labelledby" not in s]
    no_role = [s for s in svgs if 'role="img"' not in s]
    if missing:
        fail("UXI-13 / G3-20", f"{len(missing)} of {len(svgs)} <svg> elements",
             "An SVG doodle has no accessible name.",
             "A generated doodle is never decorative — it is an interpretation of "
             "what a person said. Give every one an aria-label.")
    else:
        ok("UXI-13 / G3-20",
           f"all {len(svgs)} <svg> doodles carry an aria-label")
        if no_role:
            ask("UXI-13 / G3-20", f"{len(no_role)} of {len(svgs)} <svg> elements",
                "aria-label is present but role=\"img\" is not. Without an explicit "
                "role, AT exposure of an SVG's accessible name is inconsistent.",
                "Add role=\"img\"? Also: the labels say what the doodle depicts "
                "(\"hand-drawn tangled scribble\") but not what it was derived from, "
                "which is the second half of what UXI-13 asks for.")


def check_engagement(src):
    """UXI-05 / G3-25 — no engagement mechanics."""
    pat = re.compile(r"streak|day \d+ of|notification|reminder", re.I)
    hits = set(m.group(0).lower() for m in pat.finditer(src))
    # the artifact legitimately states it has none of these; exclude negations
    real = [h for h in hits
            if not re.search(r"(no|zero|without|never)[^.]{0,40}" + re.escape(h),
                             src, re.I)]
    if real:
        fail("UXI-05 / G3-25", ", ".join(sorted(real)),
             "Engagement-mechanic vocabulary present.",
             "Unobserved: a drawer, not a dashboard. No streaks, counters, "
             "notifications, reminders or share affordances.")
    else:
        ok("UXI-05 / G3-25", "no engagement mechanics")


# ================================================================ main
def main():
    target = sys.argv[1] if len(sys.argv) > 1 else \
        "prototypes/doodle-journal/doodle-journal.html"

    if not os.path.isfile(target):
        print(f"BROKEN — no such file: {target}")
        print("Run from the repo root, or pass a path.")
        return 5

    src = load(target)
    css = style_blocks(src)
    css_rules = list(rules(css))

    check_contrast(css_rules)
    check_shadows(css)
    check_radius(css)
    check_emoji(src)
    check_focus(css)
    check_reduced_motion(css)
    check_hardcoded_hex(src, css)
    check_doodle_alt(src)
    check_engagement(src)

    print(f"check-design.py — {target}")
    print(f"{len(css_rules)} CSS rules parsed\n")

    if violations:
        print(f"=== {len(violations)} VIOLATION(S) ===\n")
        for rule, where, detail, fixtxt in violations:
            print(f"  [{rule}]  {where}")
            print(f"      what : {detail}")
            print(f"      fix  : {fixtxt}\n")

    if unresolved:
        print(f"=== {len(unresolved)} UNRESOLVED — a person must settle these ===\n")
        for rule, where, detail, question in unresolved:
            print(f"  [{rule}]  {where}")
            print(f"      what : {detail}")
            print(f"      ask  : {question}\n")

    if moot:
        print("=== MOOT — the rule has nothing to act on yet ===\n")
        for rule, detail in moot:
            print(f"  [{rule}] {detail}\n")

    if passes:
        print("=== PASS ===")
        for rule, detail in passes:
            print(f"  [{rule}] {detail}")
        print()

    print("Not checked here, because a static read cannot settle it: target size, "
          "focus-ring visibility in practice, keyboard order, reading order, the "
          "eight states, composition rules C-01..C-12, and response-time budgets. "
          "A clean run is not an audit.")

    if violations:
        print(f"\nBLOCKED — {len(violations)} design-system violation(s).")
        return 6
    if unresolved:
        print(f"\n{len(unresolved)} unresolved. No violations found.")
        return 7
    print("\nNo violations.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
