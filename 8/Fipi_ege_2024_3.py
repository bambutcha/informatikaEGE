from itertools import*

k=0
l=0
for x in product(sorted('ФЛАМИНГО'),repeat = 5):
    s = ''.join(x)
    k += 1
    if k%2 != 0 and s[0]!= 'Н' and s.count('О') <= 1:
        l += 1
print(l)
