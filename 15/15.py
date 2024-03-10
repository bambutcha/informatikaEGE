def f(x):
    return ((x**2 - 11*x + 28) > 0) or ((y**2 - 9*y +14) > 0) or ((x**2 + y**2) > a)

for a in range(1,100000):
    if all(f(x,y) == 1 for x in range(1,1000) for y in range(1,1000)):
        print(a)
