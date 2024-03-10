def f(n):
    if n <=3:
        return 1
    if n > 3:
        return (n+1) + f(n-2)

print(f(2028) - f(2024))
