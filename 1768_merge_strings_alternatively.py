
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
    while(len(s1) > index):
        s3.append(s1[index])
        index+=1
    while(len(s2) > index):
        s3.append(s2[index])
        index+=1
    s3 = "".join(s3)
    return s3

# s1 = "abc"
# s2 = "pqr"
# s1 = "abcd"
# s2 = "pq"
s1 = "ab"
s2 = "spqr"
print(merge_string(s1, s2))