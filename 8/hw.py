from itertools import*

k = 0
l = 0
for x in product(sorted('СТЕПУХА'), repeat = 4):
    s = ''.join(x)
    k += 1
    if k > 1000 and s[0] != s[1] and s[1] != s[2] and s[2] != s[3]:
        l += 1
print(l)
