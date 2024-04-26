f = open('dosrok.txt')
k = 0

for s in f:
    a = sorted([int(x) for x in s.split()])
    if s[3] < (s[0]+s[1]+s[2]):
        if (s[0]+s[1]) == (s[2]+s[3]) or (s[1]+s[3]) == (s[0]+s[2]) or \
           (s[0]+s[3]) == (s[1]+s[2]):
            k += 1
print(k)
    
