def productOfArray(nums):
    forward = [1] * len(nums)
    backward = [1] * len(nums)
    final = [1] * len(nums)

    forward[0] = nums[0]
    backward[len(nums) -1] = nums[len(nums) -1] 
    for x in range(1, len(nums)):
        forward[x] = nums[x] * forward[x-1]
        backward[len(nums) - 1 - x] = nums[len(nums) - x - 1] * backward[len(nums)-x]

    final[0] = backward[1]
    for x in range(1, len(nums) - 1):
        final[x] = forward[x - 1] * backward[x +1]
    final[len(nums) - 1] = forward[len(nums) - 2]
    return final

nums = [1,2,3,4]
print(productOfArray(nums))
