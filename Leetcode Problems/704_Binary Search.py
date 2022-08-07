nums = [-1,0,3,5,9,12]

target = 9

# Iteration Method

def binarySearch(nums):
    for i in range(len(nums)):
        l = 0
        r = len(nums)-1
        mid = l+r//2
        if target == nums[i]:
            return i
        if target>nums[i]:
            l += mid
        if target<nums[i]:
            r -= mid
    return -1


# Recursive Method
def BinarySearch(nums,l,r,target):
    if l>r:
        return -1
    else:
        mid = (l + r) // 2
        if target == nums[mid]:
            return mid
        elif target>nums[mid]:
            return BinarySearch(nums,mid+1,r,target)
        else:
            return BinarySearch(nums,l,mid-1,target)
print(BinarySearch(nums,0,len(nums),target))
