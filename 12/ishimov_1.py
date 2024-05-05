max_num = []
for n in range(4,10000):
    s = '7' + n * '1'
    while '1111' in s or '7777' in s:
        s = s.replace('1111', '77',1)
        s = s.replace('7777', '1', 1)
    max_num.append(s.count('1')+s.count('7')*7)
print(max(max_num))
