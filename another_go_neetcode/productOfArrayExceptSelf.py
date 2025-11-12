def function(nums):
    res = [1] * len(nums)
    prefix = 1
    for x in range(len(nums)):
        res[x] = prefix
        prefix *= nums[x]
    postfix = 1
    for x in range(len(nums) - 1, -1, -1):
        res[x] *= postfix
        postfix *= nums[x]
    return res

nums = [1,2,3,4]


#Output: [48,24,12,8]

print(function(nums))


"""
    res = []
    for x in nums:
        if(x == 0):
            res.append(0)
        else:
            res.append(int(sum/x))

    return res
"""