def lin(c):
    c = c/255
    return c/12.92 if c <= 0.03928 else ((c+0.055)/1.055)**2.4
def lum(h):
    h = h.lstrip('#')
    r,g,b = (int(h[i:i+2],16) for i in (0,2,4))
    return 0.2126*lin(r)+0.7152*lin(g)+0.0722*lin(b)
def ratio(a,b):
    la,lb = lum(a),lum(b)
    hi,lo = max(la,lb),min(la,lb)
    return (hi+0.05)/(lo+0.05)

P = {
 'vermillion':'#D8472B','ultramarine':'#1F3C96','ochre':'#C99A2E',
 'violet':'#5B3A7E','green-earth':'#5E7A3F','cadmium':'#E8B93A',
 'ink':'#1a1612','paper':'#efe7d6','card':'#f7f0df',
}
bgs = ['paper','card','ink']
print("fg           " + "".join(f"{b:>14}" for b in bgs))
for name,hexv in P.items():
    row = f"{name:<13}"
    for b in bgs:
        r = ratio(hexv, P[b])
        flag = "AA" if r>=4.5 else ("AA-lg" if r>=3 else "FAIL")
        row += f"{r:>8.2f} {flag:<5}"
    print(row)
