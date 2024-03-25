def f(x):
    s = ''
    while x:
        ost = str(x%3)
        s = ost + s
        x = x // 3
    return s

for n in range(1, 100000):
    b = f(n)
    if n % 3 == 0:
        b = b + b[-2] + b[-1]
    if n % 3 != 0:
        c = f((n % 3) *2)
        b = b + c
    r = int(b,3)
    if r <= 325:
        print(r)
        
        
