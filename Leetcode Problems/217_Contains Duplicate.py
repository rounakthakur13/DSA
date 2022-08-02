nums= [1,5,-2,-4,-4]
visited = set()
def containsduplicate(nums):
    for i in range(len(nums)):
        if nums[i] in visited:
            return True
        else:
            visited = nums[i]
    return False
print(containsduplicate(nums)) 