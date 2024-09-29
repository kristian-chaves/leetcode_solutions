def uniqueNum(arr):
    arr.sort()
    prevNum = arr[0]
    sequentialCount = 1
    numsDict = {}

    for x in arr:
        if(prevNum == x):
            sequentialCount+=1
        else:
            numsDict[prevNum] = sequentialCount
            sequentialCount = 1
        prevNum = x
    numsDict[prevNum] = sequentialCount

    #iterate throuhg hashmap for unique values
    valuesDict = dict.fromkeys(numsDict.values())
    return len(valuesDict) == len(numsDict)

arr = [5,-2,-2,1,5,-2]
print(uniqueNum(arr))