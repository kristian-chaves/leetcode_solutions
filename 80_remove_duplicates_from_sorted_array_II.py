
def removeDupe2(nums):
    x = 2
    while x < len(nums): 
        if(nums[x-2] == nums[x-1] == nums[x]):
            nums.pop(x)
            x -= 1
        x+=1
    return len(nums) 

nums = [0,0,1,1,1,1,2,3,3]
print(removeDupe2(nums))

