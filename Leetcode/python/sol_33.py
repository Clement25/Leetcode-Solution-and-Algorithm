# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 10:50:57 2019

@author: DELL
"""

class Solution:
    def search(self, nums: 'List[int]', target: 'int') -> 'int':
        if not nums:
            return -1
        
        def bisearch(nums, start, end, target):
            if end == start:
                if nums[start] == target:
                    return start
                else:
                    return -1
            
            if target>nums[end] and target<nums[start]:
                return -1
            
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid]>target:
                # 判断前后是否为升序序列
                if nums[start]==target:
                    return start
                elif nums[start]>target and nums[start]<=nums[mid]:
                    return bisearch(nums,mid+1,end,target)
                else:
                    return bisearch(nums,start,max(start,mid-1),target)
                
            else: # nums[mid]<target
                if nums[end]==target:
                    return end
                elif nums[end]>nums[mid] and nums[end]<target:
                    return bisearch(nums,start,max(start,mid-1),target)
                else:
                    return bisearch(nums,mid+1,end,target)
        
        return bisearch(nums,0,len(nums)-1,target)

s = Solution()
a = [4,5,6,7,8,1,2,3]
b = 8
print(s.search(a,b))