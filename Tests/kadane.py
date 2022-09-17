def maxsum(a):
    currsum = 0
    maxsum = 0
    for i in range(len(a)):
        if currsum < 0:
            currsum = 0
        currsum += a[i]
        maxsum = max(currsum, maxsum)
    return maxsum


a = [-2, -1]
print(maxsum(a))
