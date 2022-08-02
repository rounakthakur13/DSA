height = [1,8,6,2,5,4,8,3,7]
l = 0
r = len(height)-1
res = 0
maxheight = 0
currheight = 0
for i in range(len(height)):
    currheight = min(height[l],height[r])*(r-l)
    if height[l]>height[r]:
        r -=1
    else:
        l += 1
    if maxheight<currheight:
        maxheight = max(currheight,maxheight)
print(maxheight)