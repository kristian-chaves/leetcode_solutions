import math

def majorityElement(nums):
    nums.sort()
    return nums[len(nums)//2]
    return 0

nums = [3,2,3]
print(majorityElement(nums))


"""
naive:
    nums.sort()
    return nums[math.floor(len(nums)/2)]
"""