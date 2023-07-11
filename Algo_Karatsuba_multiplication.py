def karatsuba(x: int, y: int) -> int:
    n = len(str(max(x,y)))
    if n == 1:
        return x*y
    deg = (n+1) // 2
    a = x // 10 ** deg
    b = x % 10 ** deg
    c = y // 10 ** deg
    d = y % 10 ** deg
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ab_cd = karatsuba(a+b, c+d) - ac - bd
    return ac * 10 ** (2*deg) + ab_cd * 10 ** deg + bd