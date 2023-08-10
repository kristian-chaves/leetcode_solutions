def isValid(s: str) -> bool:
    open = ['(', '{', '[']
    close = [')', '}', ']'] 
    p_list = []
    for i in s:
        if i in open:
            p_list.append(i)
        elif i in close:
            #check for equal index
            y = close.index(i)
            if (len(p_list)>0 and open[y] == p_list[len(p_list)-1]):
                p_list.pop()
            else:
                return False
        else:
            return False
    if(len(p_list) > 0):
        return False
    return True



print(isValid("()[]"))