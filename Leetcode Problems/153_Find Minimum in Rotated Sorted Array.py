def findmin(nums):
    l = 0
    r = len(nums) - 1
    while l < r:
        m = (l+r)//2
        if nums[m]<=nums[r]:
            r = m
        else:
            l = m+1
    print(nums[l])
nums = [4,5,6,7,8,1,2,3]
findmin(nums)