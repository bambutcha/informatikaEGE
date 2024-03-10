lown = []
z = 0
for x in range (4,2000):
    s = '2' + x * '5'
    v = int(s)
    while '25' in s or '35' in s or '555' in s:
        if '25' in s:
            s = s.replace('25', '53',1)
        if '35' in s:
            s = s.replace('35', '2',1)
        if '555' in s:
            s = s.replace('555', '23',1)
        
    while v:
        z = z + (int(v) % 10)
        v = v // 10
    if z  % 7 == 0:
        lown.append(x)
print(min(lown))
