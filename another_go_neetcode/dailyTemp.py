def function(temperatures):
    tempStack = [] #val, index
    res = [0] * len(temperatures)
    counter = 0
    for x in range(len(temperatures)):
        while tempStack and tempStack[-1][0] < temperatures[x]:
            res[tempStack[-1][1]] = x - tempStack[-1][1]
            tempStack.pop()  
        tempStack.append([temperatures[x], x])
    return res


s = [30,38,30,36,35,40,28]

print(function(s))


'''
        if(x > localGreatest):
            while tempStack:
                res.append(len(tempStack))
                tempStack.pop()
            tempStack.append(x)
            localGreatest = x
        else:
            tempStack.append(x)
'''