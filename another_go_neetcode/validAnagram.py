def validAnagram(s, t):
    #add all letters to set, if sum of set == len(first), valid
    #breaking case: repeating letters
        # marr, marm
    # if strings are sorted they should be the exact same? whats sort runtime though
    #return sorted(s) == sorted(t)

    #ok update i looked at the hint lol nvm not this
    if(len(s) != len(t)):
        return False
    dictS, dictT = {}, {}
    for x in range(len(s)):
        dictS[s[x]] = dictS.get(s[x], 0) + 1
        dictT[t[x]] = dictT.get(t[x], 0) + 1
    return dictS == dictT


s = "anagram"
t = "nagaram"
print(validAnagram(s))