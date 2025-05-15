


def jumpGame2(nums):
    count = 0
    curIndex = 0
    while True:
        if(curIndex >= len(nums) - 1):
            return count
        if(nums[curIndex] >= len(nums) - curIndex - 1):
            return count+1
        subarray = nums[curIndex+1: nums[curIndex]+curIndex+1]
        #choose rightmost max index
        for index in reversed(range(len(subarray))):
            if subarray[index] == max(subarray):
                curIndex = curIndex + index+1
                count+=1
                break

#nums = [10,9,8,7,6,5,4,3,2,1,1,0]
nums = [2,3,1,1,4]
print(jumpGame2(nums))

