def findMaxAverage(nums, k):
    greatest = float('-inf')
    window = nums[0:k]
    lp = 0
    rp = len(nums) - 1
    for x in range(k, len(nums)+1):
        greatest = max(sum(nums[(x-k):x])/k, greatest)
    return greatest


nums = [1,12,-5,-6,50,3]
k = 4

print(findMaxAverage(nums, k))