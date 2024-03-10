def f(x):
    return (a+x > 700 - a) and ((a%100) + (100%x) > 50)

for a in range(1,100000):
    if all(f(x) for x in range(1,1000)):
        print(a)