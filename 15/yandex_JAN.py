def f(x, y, a):
    return (x + 3*y < a) or (y > x) or (x > 80)

for a in range(1, 10000):
    if all(f(x, y, a) for x in range(1, 1000) for y in range(1, 1000)):
        print(a)
