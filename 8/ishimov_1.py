from itertools import *
k = 0
for x in product('0123456', repeat = 6):
    s = ''.join(x)
    if s[0] != '0':
        if s.count('3') == 1:
            s = s.replace('1','#').replace('3','#').replace('5','#')
            if '##' not in s:
                k += 1
print(k)
