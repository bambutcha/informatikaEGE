from itertools import permutations
k = 0
cnt = 0
for x in set(permutations('СОВЕСТЬ')):
    s = ''.join(x)
    for g in 'ОЕЬ':
        s = s.replace(g, 'О')
    for sg in 'СВТ':
        s = s.replace(sg, 'С')
    if not('СС' in s and 'ОО' in s):
        cnt += 1
print(cnt)
