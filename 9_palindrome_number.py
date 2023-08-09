
x = 404
s = str(x)

for i in range(0, len(s)):
    if(s[i] != s[len(s)-1-i]):
        print("False")
        #return False
print("True")
#return True
