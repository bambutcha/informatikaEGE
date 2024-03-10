a = [int(x) for x in open('pro100ege_6.txt')]
m = max(x for x in a if abs(x) % 1000 == 221)
t = []
for i in range(len(a) -2):
    x, y, z = a[i], a[i+1], a[i+2]
    pred_x, pred_y, pred_z = abs(x) // 10 % 10, abs(y) // 10 % 10, abs(z) // 10 % 10
    if (pred_x % 2 != 0) + (pred_y % 2 != 0) + (pred_z % 2 != 0) == 2:
        if (9 < abs(x) < 100) + (9 < abs(y) < 100) + (9 < abs(z) < 100) <= 2:
            if x + y + z > m:
                t.append(x + y + z)
print(len(t), min(t))
