class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        dp = [nums[0]]
        
        for i in range(1, len(nums)):
            if nums[i] > dp[-1]:
                dp.append(nums[i])
            elif len(dp) == 1 and nums[i] < dp[0]:
                dp[0] = nums[i]
            else:
                # binary search, find the first element larger than nums[i]
                start = 0
                end = len(dp) - 1
                while(start < end):
                    mid = (start + end) // 2
                    if dp[mid] < nums[i]:
                        start = mid + 1
                    else:
                        end = mid
                dp[end] = nums[i]
        return len(dp)
        
