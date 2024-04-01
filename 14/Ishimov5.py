for x in '0123456789ABCDEFGH':
    s = int(f'71{x}264', 18) + int(f'4{x}51{x}1', 18) + int(f'21{x}637',18)
    if s%17 ==0:
        print(s//17)
