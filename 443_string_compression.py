def stringComp(chars):
    writePointer = 0
    readPointer = 0

    while(readPointer < len(chars)):
        char = chars[readPointer]
        count = 0
        while readPointer < len(chars) and chars[readPointer] == char:
            readPointer += 1
            count += 1
        #update with new values
        chars[writePointer] = char
        writePointer +=1
        if(count > 1):
            for digit in str(count):
                chars[writePointer] = digit
                writePointer += 1
    #truncate post write pointer
    chars = chars[:writePointer]
    return writePointer


#chars = ["a","a","b","b","c","c","c"]
chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]

print(stringComp(chars))
print(chars)
