def f(a,m):
    if a <= 116: return m%2 == 0
    if m == 0: return 0
    h = [f(a-7, m-1), f(a//3, m-1)]
    return any(h) if m%2 != 0 else all(h)

print(max(s for s in range(117, 10000) if (f(s,3) == 1) and (f(s,1) == 0)))

print([s for s in range(117,10000) if (f(s,3) == 1) and (f(s,1) == 0)])

print([s for s in range(117,10000) if (f(s,4) == 1) and (f(s,2) == 0)])
