from collections import Counter, defaultdict

def function(nums, k):
    frequency = Counter(nums)
    mostFrequent = []
    for x in frequency.most_common(k):
        mostFrequent.append(x[0])
    return mostFrequent

#the other approach is probably iterate through the list and 
    # have a dictionary containing {number: frequency} and
    # a list of most frequent elements of k length --
    # if a value being added is greater than whatever is in the k-1th
    # position of the list, shift everything down -> return list at end

nums = [7,7]
k = 1


print(function(nums, k))