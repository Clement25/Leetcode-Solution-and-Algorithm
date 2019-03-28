# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 14:02:02 2018

@author: DELL
"""

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = point = ListNode(0)
        newl = []
        for l in lists:
            p = l
            while p is not None:
                newl.append(p.val)
        
        newl.sort()
        for i in newl:
            point.next=ListNode(val)
            point=point.next
        return head.next