# def find_sum(n):
#     if n == 1:
#         return 1
#     return n + find_sum(n-1)
    
# print(find_sum(5))
    
def fibo(n):
    if n == 1 or n == 0:
        return n
    return fibo(n-1) + fibo(n-2)
print(fibo(5))