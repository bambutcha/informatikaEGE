def f(c):
    if len(str(c)) == 4:
        return 1
    else:
        return 0


a = [int(x) for x in open('kim.txt')]
m = max(x for x in a if abs(x)%100 == 22)
t = []
for i in range(len(a) -2):
    if (f(a[i]) + f(a[i+1]) + f(a[i+2])) ==2:
        if a[i] + a[i+1] +a[i+2] <= m:
            t.append(a[i] + a[i+1] +a[i+2])
print(len(t), max(t))
