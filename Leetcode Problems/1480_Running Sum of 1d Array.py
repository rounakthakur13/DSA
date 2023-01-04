def runningSum(nums):
    newlist = []
    n = 0
    for i in range(len(nums)):
        n += nums[i]
        newlist.append(n)
    return newlist
nums = [1,2,3,4]
print(runningSum(nums))