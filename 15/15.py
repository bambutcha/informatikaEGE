def f(x,y):
    return (x + 3*y < а) or (y >x) or (x>80)

for a in range(1,200):
    if all(f(x,y) for x in range(1,1000) for y in range(1,1000)):
        print(a)
