nums = [-1,-100,3,99]
k = 5
k = k%len(nums)
l = 0
r = len(nums)-1
while l<r:
    nums[l],nums[r] = nums[r],nums[l]
    l+=1
    r-=1
l = 0
r = k-1
while l<r:
    nums[l],nums[r] = nums[r],nums[l]
    l+=1
    r-=1
l = k
r = len(nums)-1
while l<r:
    nums[l],nums[r] = nums[r],nums[l]
    l+=1
    r-=1
print(nums)
