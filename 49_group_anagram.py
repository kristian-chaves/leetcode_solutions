from collections import defaultdict

def groupAnagram(strs):
    #create list of hashmaps, put sorted cop
    data_dict = defaultdict(list)
    for x in range(0, len(strs)):
        data_dict[''.join(sorted(strs[x]))].append(strs[x])
    l2 = []
    for x in data_dict:
        l2.append(data_dict[x])
    return l2




s = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagram(s))