def f(c,e):
    if c == e: return 1
    if c < 5 or c == 20: return 0
    return f(c-2,e) + f(c-3,e) + f(c//5,e)

print(f(41,10) * f(10,5))
