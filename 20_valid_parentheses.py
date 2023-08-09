def isValid(s: str) -> bool:
    open = ['(', '{', '[']
    close = [')', '}', ']'] 
    p_list = []
    last_p = ""
    for i in s:
        if s[i] in open:
            p_list.append(i)
            last_p = i
        elif s[i] in close:
            #check for equal index
            if(close.index[i] == last_p):
                p_list.pop()
                last_p = s[i-1]
            else:
                return False
    return True



print(isValid("()[]"))