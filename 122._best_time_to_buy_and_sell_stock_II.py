
def bestTime2(prices):
    positives = 0
    previous = prices[0]
    for x in prices:
        positives += max((x - previous), 0)
        previous = x
    return positives

nums = [7,1,5,3,6,4]
print(bestTime2(nums))

