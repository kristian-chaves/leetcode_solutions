import math

def search_insert_position(nums, target):
    lower = 0
    upper = len(nums) - 1
    while lower <= upper:
        dest = (lower + upper) // 2
        if(target == nums[dest]):
            return dest
        elif(target > nums[dest]):
            lower = dest + 1
        else : #(target > nums[dest])
            upper = dest - 1
    return lower

nums = [1,3,5,6]
target = 7
print(search_insert_position(nums, target))