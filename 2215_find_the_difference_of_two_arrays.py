def findDiff(nums1, nums2):
    nums1 = dict.fromkeys(nums1)
    nums2 = dict.fromkeys(nums2)
    removeList = []
    for x in nums1:
        if(x in nums2):
            nums2.pop(x)
            removeList.append(x)
    for x in removeList:
        nums1.pop(x)
    nums1 = list(nums1)
    nums2 = list(nums2)
    return [nums1, nums2]

nums1 = [1,2,3]
nums2 = [2,4,6]
print(findDiff(nums1, nums2))