class Solution:
    def containsDuplicate(self, nums: [int]) -> bool:
        if len(nums) != len(set(nums)):
                return True
        else:
            return False