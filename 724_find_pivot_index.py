def pivotFind(nums):
    ls  = 0
    rs = sum(nums)
    for x in range(0, len(nums)):
        rs -= nums[x]
        if(ls == rs):
            return x
        ls += nums[x]
    return -1

nums = [1,7,3,6,5,6]


print(pivotFind(nums))