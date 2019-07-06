class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i,x in enumerate(nums):
            if target <= x:
                return i
        
        return len(nums)