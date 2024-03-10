from fnmatch import *
for s in range(2024, 10**10 + 1, 2024):
    if fnmatch(str(s), '1*2715?6'):
        print(s, s// 2024)
