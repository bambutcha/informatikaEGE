a = [int(x) for x in open('17.txt')]
m = max(x for x in a if abs(x)%100 == 18)
t = []
for i in range(len(a) -2):
    if(a[i]*a[i+1]*a[i+2]) % m == 0 and \
        (len(str(a[i] == 5) or (len(str(a[i+1] == 5) or\
        (len(str(a[i+2] == 5))))))):
        t.append(a[i]*a[i+1]*a[i+2])
print(len(t), max(t))
