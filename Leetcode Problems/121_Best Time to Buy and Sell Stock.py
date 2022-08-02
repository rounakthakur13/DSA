# prices = [1,2,4]
# maxprofit = 0
# currprofit = 0
# for i in range(len(prices)):
#     for j in range(i+1,len(prices)):
#         currprofit = prices[j]-prices[i]
#         if currprofit < 1:
#             currprofit = 0
#         else:
#             maxprofit = max(maxprofit, currprofit)
# print(maxprofit)

prices = [7,6,4,3,1]
maxprofit = 0
minbuy = prices[0]
for i in range(len(prices)):
    minbuy = min(prices[i],minbuy)
    maxprofit = max(prices[i]-minbuy,maxprofit)
print(maxprofit)
