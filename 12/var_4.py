import math

def f(n):
    if n <= 1:
        return False
    for i in range(2, math.isqrt(n) + 1): ## возвращает целую часть квадратного корня из числа n
        if n % i == 0:
            return False
    return True

for n in range(3, 1001):
    s = '5' + n * '4'
    while '54' in s or '444' in s or '44444' in s:
        s = s.replace('54','64', 1)
        s = s.replace('444','6', 1)
        s = s.replace('44444','55', 1)
    if f(int(s)):
        print(n)
        
