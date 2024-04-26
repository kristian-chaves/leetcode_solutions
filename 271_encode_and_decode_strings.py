def encode(strs):
    string = ''

    for x in strs:
        string += str(len(x)) + ":" + x
    return string

def decode(s):
    strs, p = [], 0
    while p < len(s):
        j = p
        while s[j] != ":":
            j+=1
        length = int(s[p:j])
        strs.append(s[j + 1 : j + 1 + length])
        p = j + 1 + length
    return strs

strings = ["neet","code","love","you"]
strings1 = []
strings2 = [""]
print(encode(strings))
print(decode(encode(strings)))