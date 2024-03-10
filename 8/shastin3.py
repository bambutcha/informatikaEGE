from itertools import product

k = 0
for x in product('01234567', repeat = 7):
    s = ''.join(x)
    if x[0] !=  '0' and sum(y in '0246' for y in x) == 2:
        for y in '135':
            s = s.replace(y, '5')
        if '57' not in s and '75' not in s and '77' not in s:
            k+=1
print(k)
