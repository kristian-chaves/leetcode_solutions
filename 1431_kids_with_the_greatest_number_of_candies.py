def greatestCandies(candies, extraCandies):
    high = max(candies)
    arr = []
    for x in candies:
        if(x + extraCandies >= high):
            arr.append(True)
        else:
            arr.append(False)
    return arr;


candies = [2,3,5,1,3]
extraCandies = 3

print(greatestCandies(candies, extraCandies))