
def bestTime2(prices):
    positives = 0
    for x in range(len(prices) - 1):
        positives += max((prices[x+1] - prices[x]), 0)
    return positives

nums = [7,1,5,3,6,4]
print(bestTime2(nums))

