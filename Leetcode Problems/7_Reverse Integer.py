x = -1234565565454
x = abs(x)
is_neg=True if x<0 else False
res = 0
digit = 0
while x>0:
    digit = x % 10
    res = res * 10
    res = res + digit
    x = x // 10
if res<2**-31 or res>2**31:
    res = 0
print(-res if is_neg else res) 