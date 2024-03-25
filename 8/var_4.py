from itertools import*

k =0
l = 0
for x in product(sorted('ХЩЗТАВПЯ'), repeat = 6):
    s = ''.join(x)
    k += 1
    if k % 2 != 0 and s[0] == 'Т' and s.count('Х') == 2:
        l += 1
print(l)
     
    
