def productOfArray(nums):
    l2 = []
    for x in range(0, len(nums)):
        l2.append(1)
        for y in range(len(nums)):
            if(x != y):
                l2[x] *= nums[y]
    return l2

nums = [1,2,3,4]
print(productOfArray(nums))
