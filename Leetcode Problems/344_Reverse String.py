def rev_arr(arr,left,right):
    if right>left:
        rev_arr(arr,left+1,right-1)
    arr[left],arr[right]=arr[right],arr[left]
arr=[1,2,3,4,5]
rev_arr(arr,0,len(arr)-1)
print(arr)
