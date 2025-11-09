def encode(strs):
    outputString = ""
    for word in range(len(strs)):
        outputString += str(len(strs[word]))
        for x in range(len(strs[word])):
            outputString += chr(ord(strs[word][x]) + 1)
    return outputString

def decode(s):
    res = []
    tracker = -1
    while tracker < len(s):
        insertWord = ""
        for x in range(tracker + 1, int(s[tracker+1]) + 1):
            insertWord += chr(ord(s[x]) - 1)
        res.append(insertWord)
        tracker += int(s[tracker])
    return s

s = ["neet","code","love","you"]

print(decode(encode(s)))