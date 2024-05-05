max_digit = []
for n in range(1, 1000):
    b = bin(n)[2:]
    if n % 2 == 0:
        b = b + b[-2] + b[-1]
    if n % 2 != 0:
        b = '1' + b + '0'
    r = int(b,2)
    if r == 202:
        max_digit.append(n)
print(max(max_digit))
