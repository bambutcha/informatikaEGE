from fnmatch import*

k = 0
for x in range(8, 680000, 8):
    if fnmatch(str(x), '1*2*'):
        k += 1
print(k)
