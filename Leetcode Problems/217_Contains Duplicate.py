nums= [1,5,-2,-4,-4]

def containsduplicate(nums):
    visited = set()
    for i in range(len(nums)):
        if nums[i] in visited:
            return True
        else:
            visited.add(nums[i])
    return False
print(containsduplicate(nums)) 