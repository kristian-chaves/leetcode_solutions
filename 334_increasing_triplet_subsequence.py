def triplet_sequence(nums):
    num1 = num2 = float('inf')
    

    if(len(nums) <= 2):
        return False
    else:
        for x in nums:
            if(x <= num1):
                num1 = x
            elif(x <= num2):
                num2 = x
            else:
                return True
    return False

nums = [20,100,10,12,5,13]

print(triplet_sequence(nums))
