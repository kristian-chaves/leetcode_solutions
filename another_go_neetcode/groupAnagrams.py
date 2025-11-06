from collections import Counter, defaultdict

def function(s):

    valsDict = {}
    for x in s:
        valsDict[x] = Counter(x)

    secondDict = defaultdict(list)
    for word in valsDict:
        print(valsDict[word].items())
        indexableVal = tuple(sorted(valsDict[word].items()))
        secondDict[indexableVal].append(word)

    return list(secondDict.values())


#s = ["act","pots","tops","cat","stop","hat"]
s = ["",""]

print(function(s))