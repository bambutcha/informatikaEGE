from itertools import*

k =0
l = 0
for x in product(sorted('012345'), repeat = 5):
    s = ''.join(x)
    k += 1
    if s[0] != '0' and s.count('3') == 1:
        if '00' not in s and '11' not in s and '22' not in s and '33' not in s \
           and '44' not in s and '55' not in s:
            l+=1
print(l)
    
