a = [int(x) for x in open('ishimov_1.txt')]
m = max(x for x in a if abs(x) % 10 == 5 and len(str(x)) == 3)
k = 0
sumtrio = []
for i in range(len(a) - 2):
    if (a[i]% 10 == 5) + (a[i+1]% 10 == 5) + (a[i+2]% 10 == 5) == 1:
        if (a[i]+a[i+1]+a[i+2]) <= m:
            k+=1
            sumtrio.append(a[i]+a[i+1]+a[i+2])
print(k, max(sumtrio))
