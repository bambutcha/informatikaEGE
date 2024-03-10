for x in '0123456789ABCDEFGHIJKLMNOPQ':
    s = int(f'17{x}35', 27) + int(f'{x}542M', 27) + int(x,27)**3
    if s%23 ==0:
        print(s//23)