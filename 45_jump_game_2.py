
def jumpGame2(nums):
    count = 0
    curIndex = 0
    while len(nums) > 1:
        qq = curIndex + nums[curIndex]
        count +=1
        if(qq >= len(nums) -1):
            return count
        l2 = nums[curIndex+1:qq + 1]
        curIndex = curIndex + len(l2) - 1 - l2[::-1].index(max(l2)) 
    return count

nums = [1,2,1,1,1]
print(jumpGame2(nums))

