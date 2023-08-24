def twoSum(nums, target):
    elm1 = 0
    while(elm1 != len(nums) - 1):
        elm2 = elm1+1
        while (elm2 <= len(nums) -1):
            if(nums[elm1] + nums[elm2] == target):
                    return [elm1, elm2]
            else:
                elm2+=1
        elm1+=1

print(twoSum([3,2,4], 6))