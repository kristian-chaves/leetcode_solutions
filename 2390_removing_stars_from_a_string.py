def removingStars(s):
    q = []
    for element in range(0, len(s)):
        if(s[element] == "*"):
            if(len(q) > 0):
                q.pop()
        else:
            q.append(s[element])
    

    return "".join(q)


s = "leet**cod*e"

print(removingStars(s))