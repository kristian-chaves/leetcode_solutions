
def removeElement(nums, val):
    lp = 0
    rp = len(nums)
    while lp <rp:
        if(nums[lp] != val):
            lp += 1
        else:
            while True:
                rp -= 1
                if(rp <lp):
                    nums.pop(lp)
                    break
                if(nums[rp] != val):
                    nums[lp] = nums[rp]
                    lp+=1
                    break
    print(nums)
    return lp


nums = [3,3]
val = 3

print(removeElement(nums, val))