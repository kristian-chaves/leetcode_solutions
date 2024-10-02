def stringClose(word1, word2):
    if len(word1) != len(word2):
        return False    
    word1 = list(word1)
    word2 = list(word2)



    return True

word1 = "abc" 
word2 = "bca"
print(stringClose(word1, word2))