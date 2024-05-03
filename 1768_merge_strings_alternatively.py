
def merge_string(s1, s2):
    s3 = ""
    turn = 1
    index = 0
    while s1 or s2:
        if turn == 1:
            s3.append(s1.pop())
    return

s1 = "abc"
s2 = "pqr"
print(merge_string(s1, s2))