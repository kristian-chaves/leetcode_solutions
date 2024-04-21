def LongestCommon(strs): 
    print(strs)
    print(*strs)
    print(tuple(zip(*strs)))
    finalStr = "" 
    for x in zip(*strs):
        if len(set(x)) == 1:
            finalStr += x[0]
        else:
            return finalStr


print(LongestCommon(["flower","flow","flight"]))