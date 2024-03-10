def f(x):
    s = set()
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            s.add(i)
            s.add(x//i)
    return sorted(s)

for x in range(123456, 987655):
    s = f(x)
    if len(s) == 5:
        print(s)
