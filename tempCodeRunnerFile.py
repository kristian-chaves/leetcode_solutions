def maxArea(height: list):
    # 1 poter
    p1 = 0
    p2 = len(height) - 1

    width = p2 - p1
    length = min(height[p1], height[p2])
    max = width * length

    if(height[p1] <= height[p2]):
        p1 += 1
    else:
        p2 -= 1
    # make temp max, if max ever greater than temp max, return
        # otherwise increment counter
    while(p1  <= p2):
        width = p2 - p1
        length = min(height[p1], height[p2])
        temp_max = width * length
        if(temp_max > max):
            max = temp_max
        #move smaller pointer
        if(height[p1] <= height[p2]):
            p1 += 1
        else:
            p2 -= 1
    return max

list1 = [10,9,8,7,6,5,4,3,2,1]
print("Ans:")
print(maxArea(list1))