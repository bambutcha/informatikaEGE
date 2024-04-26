a = [int(x) for x in open('dosrok.txt')]

m = max(x for x in a if x%19 == 0)

ans = []
for i in range(len(a) - 1):
    if a[i]> m or a[i+1]> m:
        ans.append(a[i] + a[i+1])
print(len(ans), max(ans))
