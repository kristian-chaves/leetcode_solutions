
def lengthOfLastWord(s):
    second = False
    count = 0
    for x in reversed(s):
        if x == ' ':
            if second == True:
                return count
            pass
        else:
            count +=1
            second = True       
    return count     
qq
word = 'Hello World'
print(lengthOfLastWord(word))


