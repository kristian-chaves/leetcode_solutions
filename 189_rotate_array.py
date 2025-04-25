#gonna pretend im not working w/ python and append doesnt exist for this
#could also be solved w/ less time more space complexity w/ a second array and then adding each 
    #index to  [(index + k) % len] 

def rotateArray(nums, k):
    for x in range(0, k):
        holder = nums[len(nums) - 1]    
        for x in range(len(nums) - 1, 0, -1):
            nums[x] = nums[x-1]
        nums[0] = holder
    return nums

nums = [1,2,3,4,5,6,7]
k = 3
print(rotateArray(nums, k))

