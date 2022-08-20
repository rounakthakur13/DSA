def arr(a,b):
    repeat = [float("-inf")]*len(a)
    norepeat = {}
    for j in range(len(a)):
        norepeat = a[j]
        
    for i in range(len(norepeat)):
        if b[i] not in norepeat:
            
            
            #     repeat[i] = a[i]
            # else:
            #     norepeat[i] = a[i]
        # if len(a) != len(b):
        #     return repeat
    
    return norepeat
a = [5,6,3,2]
b = [5,6,7,2]
print(arr(a,b))