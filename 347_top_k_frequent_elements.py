def top_k_frequent(nums, k):
    dict = {}
    for x in nums:
        if x in dict:
            dict[x] += 1
        else:
            dict[x] = 1
    l1 = []
    for x in range(0, k):
        l1.append(max(dict, key=dict.get))
        dict.pop(max(dict, key=dict.get))
    return l1

nums = [1,1,1,2,2,3]
k = 2
print(top_k_frequent(nums, k))