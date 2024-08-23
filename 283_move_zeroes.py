def moveZeroes(nums):
    lp = 0;
    for rp in range(len(nums)):
        if(nums[rp]):
            nums[lp], nums[rp] = nums[rp], nums[lp]
            lp+=1               


    print(nums)
    return 0 


nums = [0,1,0,3,12]


print(moveZeroes(nums))