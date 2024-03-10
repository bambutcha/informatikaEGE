n = 3 * 4056**8 + 2*676**7-4*676**6+3*156**5-2*26**4-2024
zeros = 0

while n:
    if n % 26 == 0:
        zeros += 1
    n //= 26

print(zeros)



