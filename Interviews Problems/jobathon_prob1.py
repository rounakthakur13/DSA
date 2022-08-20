# N = 4
# K = 3
# A = { 7, 5, 7, 1 }
# def solve(N,K,A):
#     hashmap = set(A)
    
#     for i in range(N):
#         if i not in hashmap:
#             return i 
# print(solve(N,K,A))
# K = 1
# A= [2]
# N = 1
# def findKthPositive(A,K,N):

#         l, h = 0, N
#         while l < h:
#             mid = (l + h) // 2
#             if A[mid] - mid - 1 < K:
#                 l = mid + 1
#             else:
#                 h = mid
#         return h + K
# # print(findKthPositive(A,K,N))

# def finKthpositive(A,K,N):
#     N = list(range(0,N))
    
#     for i in A:
#         if i in N:
#             N.remove(i)
#     l, h = 0, len(N)
#     while l < h:
#         mid = (l + h) // 2
#         if N[mid] - mid - 1 < K:
#             l = mid + 1
#         else:
#             h = mid
#     return h + K
# # print(finKthpositive(A,K,N))


# def findKthPositive(arr,k):
#     # if the kth missing is less than arr[0]
#     arr.sort()
#     if k <= arr[0] - 1:
#         return k
#     k -= arr[0] - 1

#     # search kth missing between the array numbers
#     for i in range(len(arr) - 1):
#         # missing between arr[i] and arr[i + 1]
#         curr_missing = arr[i + 1] - arr[i] - 1
#         # if the kth missing is between
#         # arr[i] and arr[i + 1] -> return it
#         if k <= curr_missing:
#             return arr[i] + k
#         # otherwise, proceed further
#         k -= curr_missing

#     # if the missing number if greater than arr[-1]
#     return arr[-1] + k
# arr = [7,5,4,1]
# k = 4
# print(findKthPositive(arr,k))

def findKthPositive(arr,N):
    arr.sort()
    newarr = list(range(0,N))
    for i in arr:
        if i in newarr:
            newarr.remove(i)
    for j in range(0,len(arr)):
        if newarr[j]>=N:
            smallest = newarr[j]
    return smallest
arr = [7, 5, 7, 1]
N = 4
print(findKthPositive(arr,N))
# def maximumMultiple(N,A) -> int:
#     count=0
#     B=[]
#     while(count<N):
#         B.append(A[count]*A[count+1])
#         count=count+2
#     return max(B)
# print(maximumMultiple(8,[-11,8,10,9,-19,-8,19,-14]))