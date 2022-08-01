num= [-2,1,-3,4,-1,2,1,-5,4]
maxsum = num[1]
currentsum = 0
n =0 
def maxSubrray(num):
    if currentsum<0:
        currentsum = 0
    currentsum += num[n]
    maxsum = max(maxsum,currentsum)
    return maxSubrray(num[n+1])
print(maxSubrray(num))