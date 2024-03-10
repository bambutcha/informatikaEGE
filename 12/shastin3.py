highch = 0

for x in range(3,9999):
    s = '5' + x * '7'
    while '57' in s or '877' in s or '777' in s:
            s= s.replace('57', '7', 1)
            s= s.replace('877', '75', 1)
            s= s.replace('777', '8', 1)
    highch = max(highch, sum(map(int,s)))
print(ss)
        
