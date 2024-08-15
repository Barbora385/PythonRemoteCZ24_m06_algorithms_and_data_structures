Factorial:
5! = 5x4x3x2x1x
0! = 1
1! = 1
2! = 2*1
3! = 3*2*1
4! = 4*3*2*1

def fac(n: int) -> int:
    if n < 0:
        rease ValueError
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n+1):
        result