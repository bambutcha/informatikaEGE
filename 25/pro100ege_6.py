def f(x):
    divisors = []
    for i in range(1, int(x**0.5) + 1):
        if x % i == 0:
            divisors.append(i)
            if i != x // i:  # добавляем только один из парных делителей
                divisors.append(x // i)
    if len(divisors) == 5:
        return sorted(divisors[-2:])  # возвращаем два наибольших делителя
    return []

a = 123456
b = 987654
for x in range(a, b+1):
    divisors = f(x)
    if divisors:
        print(f"{divisors[1]} {x}")
