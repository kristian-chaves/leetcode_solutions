 def isAnagram(s: str, t: str):
    q = list(s)
    q.sort()
    w = list(t)
    if(len(q) != len(w)):
        return False
    w.sort()
    for x in range(len(w)):
        if(w[x] != q[x]):
            return False
    return True

print(isAnagram(s = "rat", t = "tar"))