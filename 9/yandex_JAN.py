k = 0
f = open('1.txt')
k = 0
for s in f:
    a = sorted([int(x) for x in s.split()])
    if (a[0] == a[1] and a[2] == a[3]) or (a[0] == a[3] and a[1] == a[2]) \
       or (a[0] == a[2] and a[1] == a[3]):
        k += 1
print(k)
