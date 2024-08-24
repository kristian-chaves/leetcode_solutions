def findMaxAverage(nums, k):
    window = sum(nums[:k])
    greatest = window/k    
    for x in range(k, len(nums)):
        window += nums[x] - nums[x-k]
        greatest = max(greatest, window/k)
    return greatest


nums = [5]
k = 1

print(findMaxAverage(nums, k))