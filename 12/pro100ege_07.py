minnumber = -1
for n in range(4, 10000):
    s = '1' + n*'9'
    while '19' in s or '49' in s or '999' in s:
        s = s.replace('19','9',1)
        s = s.replace('49','91',1)
        s = s.replace('999','4',1)
    k = s.count('1') + s.count('9')*9 + s.count('4')*4
    if k > minnumber:
        minnumber = k
print(minnumber)
