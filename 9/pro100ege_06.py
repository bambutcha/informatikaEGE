f = open('pro100ege_06.txt')
k = 0

for s in f:
    a = sorted([int(x) for x in s.split()])
    if (a[0]%2==0 and a[1]%2==0) + (a[1]%2==0 and a[2]%2==0) + \
                                     (a[2]%2==0 and a[3]%2==0) + \
                                      (a[3]%2==0 and a[4]%2==0) == 3:
                
