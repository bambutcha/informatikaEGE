k = 0
f = open('pro100ege_6.txt')
k = 0

for s in f:
    t = 0
    a = sorted([int(x) for x in s.split()])
    if a[1] % 2 == 0 or a[2] % 2 == 0 or a[3] % 2 == 0 or a[4] % 2 == 0:
        t + = 1
