def encode(strs):
    str = ''
    for x in strs:
        str = str + x + ","
    str = str[:-1]
    return str

def decode(s):
    return s.split(",")

strings = ["neet","code","love","you"]

print(encode(strings))
print(decode(encode(strings)))