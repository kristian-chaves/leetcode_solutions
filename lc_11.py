def maxArea(height: list):
    max = 0
    p1 = len(height)
    #iterate through array, find multiples, if multiple > max, new max
    for h1 in range(0, len(height)-1):
        for h2 in range(h1+1, len(height)):
            length = min(height[h1], height[h2])
            width = h2 - h1
            area = length * width
            if(area > max):
                max = area
    return max

list1 = [1,8,6,2,5,4,8,3,7] 
print("Ans:")
print(maxArea(list1))