def reverseWords(s):
    words = []
    words2 = []
    for x in range(0, len(s)):
        if(s[x] == " "):
            words.reverse()
            words2.append(words)
            words = []
        else:
            words.append(s[x])
    words.reverse()
    words2.append(words)
    q = ""
    words2.reverse()
    for x in words2:
        x.reverse()
        if(x != []):
            q += "".join(x)
            q += " "
    
    return q[:-1]


s = "  hello world  "

print(reverseWords(s))
