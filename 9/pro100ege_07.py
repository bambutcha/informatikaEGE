f = open('pro100ege_07.txt')
k = 0

for s in f:
    a = sorted([int(x) for x in s.split()])
    if len(set(a)) == 5:
        if ((a[0] + a[4])*2) <= (a[1]+a[2]+a[3]):
            k += 1
print(k)
                
