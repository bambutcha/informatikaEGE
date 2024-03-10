from sys import*
setrecursionlimit(12000)

def f(x):
    if x >= 10000:
        return 1
    if x < 10000 and x % 2 == 0:
        return f(x+3) + 7
    if x < 10000 and x % 2 != 0:
        return f(x+1) - 3

print(f(50) - f(57))
