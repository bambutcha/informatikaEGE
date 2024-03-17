from fnmatch import fnmatch

for n in range(7777, 10**10 + 1, 7777):
    if n % 2 == 0 and fnmatch(str(n), '12*567?'):
        print(n,n // 7777)
