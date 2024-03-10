def f(x,y):
    return not((3*x + y > a) and (y<x) and (x < 30))

for a in range(1,200):
    if all(f(x,y) for x in range(1,1000) for y in range(1,1000)):
        print(a)
