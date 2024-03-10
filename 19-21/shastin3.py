def f(a,b,m):
    if a + b >= 375: return m%2 == 0
    if m == 0: return 0
    h = [f(a + 3,b, m-1), f(a,b+3,m-1), f(a*2, b,m-1), f(a,b*2,m-1)]
    return any(h) if m%2!=0 else all(h)
print([s for s in range(1,348) if f(27,s,2)])
print([s for s in range(1,348) if f(27,s,3) > f(27,s,1)])
print([s for s in range(1,348) if f(27,s,4) > f(27,s,2)])
