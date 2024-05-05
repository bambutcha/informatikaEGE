from fnmatch import*
for x in range(98591, 10**11, 98591):
    if fnmatch(str(x), '123*45??1?'):
        print(x, x//98591)
