def f(x):
    s = ''
    while x:
        ost = str(x% 8)
        s = ost + s
        x = x //8
    return s

cumman = []
for x in range(10000, 100000):
    b = f(x)
    while '1' in b or '3' in b or '5' in b or '7' in b:
        b = b.replace('1', '2')
        b = b.replace('3', '2')
        b = b.replace('5', '2')
        b = b.replace('7', '2')
    b = b + str(x%8)
    r = int(b,8)

    z = f(int(b))
    while '1' in z or '3' in z or '5' in z or '7' in z:
        z = z.replace('1', '2')
        z = z.replace('3', '2')
        z = z.replace('5', '2')
        z = z.replace('7', '2')

    z = z + str(x%8)
    r1 = int(z,8)

    if r1 % 2023 == 0:
        print(n)
