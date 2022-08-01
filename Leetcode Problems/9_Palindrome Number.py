x = 121
num = x
digit = 0
res = 0
def palindrome(x,res,digit):
    while x>0:
        digit = x % 10
        res = res * 10
        res = res + digit
        x = x//10
    if res == num:
        return True
    else:
        return False
print(palindrome(x,res,digit))
