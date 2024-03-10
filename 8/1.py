from itertools import*

k = 0
l = 0
for x in product(sorted('РЕПЛИКА'),repeat = 6):
    s = ''.join(x)
    k += 1
    if k%2 == 0 and s[0]!= 'К' and s.count('И') >= 2:
        l += 1
print(l)
        
    
