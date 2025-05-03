
def jumpGame(nums):
    index = len(nums) - 1
    currentCheck = index
    fini = True
    while True:
        index -= 1
        if(index == -1):
            return fini
        if(currentCheck - index > nums[index]):
            fini = False
        else:
            currentCheck = index
            fini = True

nums = [2,3,1,1,4]
print(jumpGame(nums))

