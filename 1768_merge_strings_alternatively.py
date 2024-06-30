
def merge_string(s1, s2):
    s3 = []
    turn = 1
    index = 0
    while index <len(s1) and index < len(s2):
        if turn % 2 == 1:
            s3.append(s1[index])
        else:
            s3.append(s2[index])
            index += 1
        turn+=1
    if(turn % 2 == 1):
        index+=1
    if(index > s1):
        s3.append(s2)
    else:
        s3.append(s2)
    return s3

s1 = "abc"
s2 = "pqr"
print(merge_string(s1, s2))