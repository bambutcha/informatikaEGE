def f(c,e):
    if c > e: return 0
    if c == e: return 1
    if c == 18 or c == 10:
        return f(c+2,e) + f(c*2,e)
    if c < e:
        return f(c+2,e) + f(c+3,e) + f(c*2,e)

print(f(3,20))
