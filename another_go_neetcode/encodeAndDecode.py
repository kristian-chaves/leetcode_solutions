def encode(strs):
    outputString = ""
    for word in range(len(strs)):
        outputString += str(len(strs[word]))
        outputString += "_"
        for x in range(len(strs[word])):
            outputString += chr(ord(strs[word][x]) + 1)
    return outputString

def decode(s):
    res = []
    while s != "":
        tracker = 0
        length = ""
        while s[tracker] != '_':
            length += s[tracker]
            tracker += 1
        word = s[len(length) +1:int(length)+len(length) +1]
        insertWord = ""
        for x in word:
            insertWord += chr(ord(x) - 1)
        res.append(insertWord)
        s = s[int(length)+len(length) +1:]

    return res

s = ["neet","code","love","you"]

print(decode(encode(s)))