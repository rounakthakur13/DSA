num= [1]
def maxSubrray(currentsum,maxsum,n):
    if n == len(num):
        return maxsum
    if currentsum<0:
        currentsum = 0
    currentsum += num[n]
    maxsum = max(maxsum,currentsum)
    return maxSubrray(currentsum,maxsum,n+1)
print(maxSubrray(num[0],0,1))