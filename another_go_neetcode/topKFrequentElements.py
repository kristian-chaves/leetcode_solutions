from collections import Counter, defaultdict

def function(nums, k):
    frequency = Counter(nums)
    mostFrequent = []
    for x in frequency.most_common(k):
        mostFrequent.append(x[0])
    return mostFrequent


nums = [7,7]
k = 1


print(function(nums, k))