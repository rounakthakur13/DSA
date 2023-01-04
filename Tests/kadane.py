def maxsum(nums):
    currsum = nums[0]
    maxsum = nums[0]
    for i in range(1,len(nums)):
        if currsum < 0:
            currsum = 0
        currsum += nums[i]
        maxsum = max(currsum, maxsum)
    return maxsum


nums =[1]
print(maxsum(nums))
