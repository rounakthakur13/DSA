k = 2
arr = [1,2,3,4,5]
newarr = []
for i in range(len(arr)):
    newarr.append(arr[k%len(arr)])
    k +=1 
print(newarr)