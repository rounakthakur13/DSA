# n1=0
# n2=1
# res = 0
# n = 69
# count = 0
# def fibo(n1,n2,res,count):
#     if count>=n-1:
#         print(res)
#         return 
#     res = n1+n2
#     n1= n2
#     n2 = res
#     count+=1
#     fibo(n1,n2,res,count)
# fibo(n1,n2,res,count)
memory = {}
def fibo(n):
    if n in memory:
        return memory[n]
    if n == 0:
        return 0
    if n == 1:
        return 1
    memory[n] = fibo(n-1)+fibo(n-2)
    return memory[n]
print(fibo(600))
