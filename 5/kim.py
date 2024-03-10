def f(x):
    s = ''
    while x:
        ost = str(x % 2)
        s = ost + s
        x = x // 2
    return s

for n in range (1, 3000):
    b = f(n)
    if n % 2 == 0:
        b = b + b[0] + b[1]
    if n % 2 != 0:
        b = "1" + b + "1"
    r = int(b,2)
    if r < 100:
        print(n)
