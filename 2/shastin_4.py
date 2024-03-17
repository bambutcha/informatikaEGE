print('x y z w')
for w in range(0,2):
    for x in range(0,2):
        for y in range(0,2):
            for z in range(0,2):
                f = (not(x == w and (not(z)))) and (y==x and (not(w)))
                if f == 1:
                    print(w,x,y,z)
