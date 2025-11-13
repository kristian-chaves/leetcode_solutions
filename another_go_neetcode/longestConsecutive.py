def function(nums):
    longestCount = 0
    currentCount = 0
    entriesDict = {}
    visitedSet = set()
    #add to entries dict, then iterate - attain maximum -> work down -- if chain with it exists, skip
    for x in nums:
        entriesDict[x+1] = x
    
    for x in nums:
        if x not in visitedSet:
            # chain to the top
            chainActive = True
            while chainActive:
                if(x+1 in entriesDict):
                    x+=1
                else:
                    chainActive = False    
            #start chaining down
            chainActive = True
            while chainActive:
                if x in entriesDict:
                    currentCount += 1
                    x = entriesDict[x]
                    visitedSet.add(x)
                else:
                    chainActive = False
            longestCount = max(longestCount,currentCount)
            currentCount = 0
    return longestCount


s = [2,20,4,10,3,4,5]

print(function(s))