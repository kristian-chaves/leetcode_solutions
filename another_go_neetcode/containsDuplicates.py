def containsDupes(s):
    #make into set, compare size of set and default
    if (len(s) == len(set(s))):
        return False
    else:
        return True


s = [1, 2, 3, 3]

print(containsDupes(s))