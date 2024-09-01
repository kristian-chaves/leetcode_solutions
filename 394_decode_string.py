
def decodeString(s):
    final = []

    for x in range(len(s)):
        if(s[x] != "]"):
            final.append(s[x])
        else:
            q = ""
            while final[-1] != "[":
                q = final.pop() + q
            final.pop()

            num = ""
            while final and final[-1].isdigit():
                num += final.pop()
            num = num[::-1]

            final.append(int(num) * q)            
    return "".join(final)


s = "3[a]2[bc]"

print(decodeString(s))

