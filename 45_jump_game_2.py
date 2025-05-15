


def jumpGame2(nums):
    count = 0
    curIndex = 0
    while True:
        if(curIndex >= len(nums) - 1):
            return count
        subarray = nums[curIndex+1: nums[curIndex]+curIndex+1]
        #choose rightmost max index
        for index in reversed(range(len(subarray))):
            if subarray[index] == max(subarray):
                curIndex = curIndex + index+1
                count+=1
                break

nums = [1,2,1,1,1]
print(jumpGame2(nums))

