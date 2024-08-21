def reverseVowels(s):
    vowels = []
    arr = []
    for x in range(0, len(s)):
        if s[x].lower() in ("a", "e", "i", "o", "u"):
            vowels.append(s[x])
            arr.append(-1)
        else:
            arr.append(s[x])

    for x in range(0, len(arr)):
        if(arr[x] == -1):
            arr[x] = vowels.pop()
    return "".join(arr)


s = "0P"

print(reverseVowels(s))