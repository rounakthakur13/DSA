nums = [2,2,1]
duplicate = []
for i in nums:
    if i not in duplicate:
        duplicate.append(i)
    else:
        duplicate.remove(i)
print(duplicate.pop())

