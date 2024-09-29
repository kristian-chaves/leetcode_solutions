def bestTime(prices, fee):
    maxProfit = 0
    lowestPrice = float('inf')
    greatestPrice = float('-inf')
    for x in prices:
        if(x < lowestPrice):
            lowestPrice = x
            greatestPrice = x
        if(x > greatestPrice):
            greatestPrice = x
        maxProfit = max(maxProfit,(greatestPrice - lowestPrice - fee))
    return maxProfit

prices = [1,3,2,8,4,9]
fee = 2
print(bestTime(prices, fee))