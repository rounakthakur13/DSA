def kidsWithCandies(candies,extraCandies):
    newlist = []
    n = 0
    for i in range(len(candies)):
        if candies[i]+extraCandies > n:
            newlist.append(True)
        else:
            newlist.append(False)
        n = candies[i]+extraCandies
    return newlist
candies = [2,3,5,1,3]
extraCandies = 3
print(kidsWithCandies(candies,extraCandies))
