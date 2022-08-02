def palin(n):
    pal_n=0
    while n:
        pal_n*=10
        pal_n+=n%10
        n//=10
    return pal_n
print(palin(123))