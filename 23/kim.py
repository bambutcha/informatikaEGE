def f (c,e):
    if c == e: return 1
    if c > e or c == 12: return 0
    return f(c+1,e) + f(c*2,e) + f(c**2,e)

print(f(2,23)*f(23,42))
    
