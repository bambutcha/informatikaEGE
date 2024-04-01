def f(x):
    return ((x%15==0) and (not(x%10==0))) <= (a < (x + 50))

for a in range(1,100000):
    if all(f(x) for x in range(1,1000)):
        print(a)
