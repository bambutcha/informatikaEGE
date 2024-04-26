from itertools import *
k = 0
for x in product(sorted('ПАРУС'), repeat = 5):
    s = ''.join(x)
    k+=1
    if s.count('У') <= 1 and 'АА' not in s:
        print(k)
