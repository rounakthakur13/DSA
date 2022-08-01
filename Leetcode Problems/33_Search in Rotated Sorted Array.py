def search(nums,target):
        l = 0
        r = len(nums) - 1
        while l <= r:

            m = (l+r)//2
            if nums[m] == target:
                return True
            if nums[l]<=nums[m]:
                if nums[l]<=target and target<=nums[m]:
                        r = m-1
                else:
                        l = m+1
            elif nums[r]>=target and target>=nums[m]:
                l = m+1
            else:
                r = m - 1
        return False
nums = [4,5,6,7,0,1,2]
target = 2
print(search(nums,target))