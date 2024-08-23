def isSubsequence(s, t):
    indexS, indexT = 0, 0
    while(indexS < len(s) and indexT < len(t)):
        if(t[indexT] == s[indexS]):
            indexS+=1
        indexT+= 1

    return indexS == len(s)


s = "axc"
t = "ahbgdc"


print(isSubsequence(s, t))