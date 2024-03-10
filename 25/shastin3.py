from fnmatch import*
for s in range(1777, 10**10 + 1, 1777):
    if fnmatch(str(s), '21*68?79'):
        print(s, s // 1777)
