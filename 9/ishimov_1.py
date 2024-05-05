f = open('ishimov_1.txt')
k = 0

for s in f:
    a = sorted([int(x) for x in s.split()])
    for x in (len(a)):
        if a.count(x) == 3
