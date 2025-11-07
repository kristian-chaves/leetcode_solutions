from collections import Counter, defaultdict

def function(nums, k):
    mostFrequent = [[] for i in range(len(nums) +1)]
    frequencyDict = defaultdict(int)
    for x in nums:
        frequencyDict[x] +=  1
    for x, y in frequencyDict.items():
        mostFrequent[y].append(x)
    res = []
    for i in range(len(mostFrequent) - 1, 0, -1):
        for n in mostFrequent[i]:
            res.append(n)
            if(len(res) == k):
                return res


nums = [3,1,3,2,2,3]
k = 2


print(function(nums, k))