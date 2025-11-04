def twoSum(nums, target):
    # go through the list, if x not in dictionary add to dictionary as [target - nums[x], x]
    # check if 
    numDict = {}
    for x in range(0, len(nums)):
        if(nums[x] in numDict):
            return [numDict[nums[x]], x]
        else:
            numDict[target - nums[x]] = x 
    return


nums = [3,4,5,6]
target = 7


print(twoSum(nums, target))