cnt = 0
f = open('9.txt')

for s in f:
    t = 0
    a = sorted([int(x) for x in s.split()])
    if len(set(a)) == len(a) - 1 and a.count(max(a)) == a.count(min(a)):
        cnt +=1
print(cnt)
