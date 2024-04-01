from intlib import *
for x in range(1,58):
    for y in range(0,72):
        s = from_base(int(f'34{x}5')) + from_base(int(f'12{x}7')) + from_base(int(f'{x}456',67)) - from_base(int(f'{x}5{y}7',72))
        if s > 0 and s % 363 == 0:
            print(x+y)

