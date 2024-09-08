def bestTime(prices):
    maxProfit = 0
    lowestPrice = float('inf')
    greatestPrice = float('-inf')
    for x in prices:
        if(x < lowestPrice):
            lowestPrice = x
            greatestPrice = x
        if(x > greatestPrice):
            greatestPrice = x
        maxProfit = max(maxProfit,(greatestPrice - lowestPrice))
    return maxProfit

prices = [7,1,5,3,6,4]
print(bestTime(prices))