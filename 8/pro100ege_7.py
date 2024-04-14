from itertools import*

k = 0
l = 0
for x in permutations('0123456789', r = 6):
    s = ''.join(x)
    if s[0] != '0':
        k += 1
        if int(s) % 5 == 0:
            if all(s.count(x) == 1 for x in s):
                s = s.replace('0', '*').replace('2', '*').\
                    replace('4', '*').replace('6', '*').replace('8', '*')
                s = s.replace('1','#').replace('3','#').\
                    replace('5','#').replace('7','#').replace('9','#')
                if '**' not in s and '##' not in s:
                    l+=1
print(l)
