def LongestCommon(strs): 
    finalStr = "" 
    for x in range(len(strs[0])):
        for s in strs:
            if len(s) == x or s[x] != strs[0][x]:
                return finalStr
        finalStr += strs[0][x]
    return finalStr


print(LongestCommon(["flower","flow","flight"]))