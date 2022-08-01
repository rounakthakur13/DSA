def maxProduct(nums):
    max_subarray = nums[0]
    min_subarray = nums[0]
    maxprod = nums[0]
    for i in range (1,len(nums)):
        # temp_maxsubarray = max_subarray
        # max_subarray = max(nums[i],min_subarray*nums[i],max_subarray*nums[i])
        # min_subarray = min(nums[i],min_subarray*nums[i],temp_maxsubarray*nums[i])
        max_subarray, min_subarray = max(nums[i],min_subarray*nums[i],max_subarray*nums[i]),min(nums[i],min_subarray*nums[i],max_subarray*nums[i])

        maxprod = max(maxprod,max_subarray)
       # print(max_subarray,min_subarray,maxprod)
    return maxprod
nums = [-4,-3,-2]
print(maxProduct(nums))