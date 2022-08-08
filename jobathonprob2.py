# N = 4
# A = [-12, 17, -13, 17]
# sum = float("-inf")
# for i in range(0,len(A),2):
#     print(A[i]*A[i-1])
#     sum = max(sum,A[i]*A[i-1])
# print(sum)
A=[2,6]
A.sort()
l=0
r=len(A)-1
res=A[l]*A[r]
while l<r:
    l +=1
    r -=1
    res=max(res,A[l]*A[r])
print('ANS' , res)