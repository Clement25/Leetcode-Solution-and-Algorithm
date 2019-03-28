# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 13:17:58 2018

@author: DELL
"""
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        l = len(lists)
        if l==1:
            return lists[0]
        elif l>2:
            mid = int (l/2)
            return self.mergeKLists([self.mergeKLists(lists[0:mid]),self.mergeKLists(lists[mid:])])
        else:
            if lists[0].val<lists[1].val:
                head=lists[0]
                p2 = lists[1]
            else:
                head=lists[1]
                p2 = lists[0]
            p1 = head
            while p1.next is not None and p2 is not None:
                if p2.val>=p1.val and p2.val<p1.next.val:
                    temp = p2.next
                    p2.next=p1.next
                    p1.next=p2
                    p1=p1.next
                    p2=temp
                else:
                    p1=p1.next
            if p2 is not None:
                p1.next=p2
            return head
        
def main():
    head1 = ListNode(3)
    head1.next=ListNode(5)
    head1.next.next=ListNode(7)
    head2 = ListNode(4)
    head2.next=ListNode(6)
    head2.next.next=ListNode(8)
    head3=ListNode(2)
    head3.next=ListNode(4)
    head3.next=ListNode(8)
    s=Solution()
    f=s.mergeKLists([head1,head2,head3])
    p = f
    while p is not None:
        print(p.val)
        p=p.next

if __name__=='__main__':
    main()