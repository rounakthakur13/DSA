nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
def merge(nums1,n,nums2,m):
    newarr = [0]*(m+n)
    l = 0
    r = 0
    for i in range(0,m+n):
 
        if nums1[l]<=nums2[r] and l <= m:
            newarr[i] = nums1[l]
            l+=1
        elif nums2[r]<=nums1[l] and r <=n:
            newarr[i] = nums2[r]
            r+=1
        else:
            break
    return newarr


print(merge(nums1,n,nums2,m))