class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def constructListNode(nums):
    head = ListNode(nums[0])
    lp = head
    for i in nums[1:]:
        new = ListNode(i)
        lp.next = new
        lp = lp.next
    return head


def removeNthFromEnd(head, n):
    """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
    v = []
    h = head
    while h is not None:
        v.append(h.val)
        h = h.next
    #length=1 return None
    if len(v) == 1:
        return None
    val = v[len(v) - n]
    #value in head equals val
    if head.val == val:
        return head.next
    #otherwise, visit the linknode until find the value
    h = head
    while h.next.val != val:
        h=h.next
    h.next = h.next.next
    return head


LinkList = constructListNode([1, 2, 3, 5])
a = removeNthFromEnd(LinkList, 2)

while a != None:
    print(a.val)
    a = a.next
