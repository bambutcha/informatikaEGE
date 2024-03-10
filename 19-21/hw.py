from sys import*
setrecursionlimit(1000000)

def f(c,e,k):
    if c > e or c < 0: return 0
    if c == e and (k >7 or k < 7) : return 0
    if c == e and k ==7 : return 1
    if c < e: return f(c-5,e,k+1) + f(c+2,e,k+1) + f(c**2, e, k+1)

print(f(3,28,0))
