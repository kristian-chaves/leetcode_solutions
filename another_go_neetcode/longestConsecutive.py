def function(nums):
    longestCount = 0
    entriesDict = {}
    visitedSet = set()

    for x in nums:
        entriesDict[x+1] = x
    
    for x in nums:
        if x not in visitedSet:
            currentCount = 0
            while(x+1 in entriesDict):
                x+=1
            while x in entriesDict:
                currentCount += 1
                x = entriesDict[x]
                visitedSet.add(x)
            longestCount = max(longestCount,currentCount)
    return longestCount


s = [2,20,4,10,3,4,5]

print(function(s))