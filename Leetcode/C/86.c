/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode *partition(struct ListNode *head, int x)
{
    struct ListNode *ptr, *pre, *nhead, *nptr;
    //a flag indicating if ptr equals head address;
    bool ptr_head = true;
    //must allocate once, or pre doesn't have the 'next' pointer
    pre = (struct ListNode *)malloc(sizeof(struct ListNode));
    nhead = NULL;
    ptr = head;
    pre->next = head;

    //Basic idea: expel all elements no less than x into a new linklist
    while (ptr != NULL)
    {
        if (ptr->val >= x)
        {
            if (nhead == NULL)
            {
                nhead = ptr;
                nptr = nhead;
            }
            else
            {
                nptr->next = ptr;
                nptr = nptr->next;
            }
            //update previous linklist
            if (ptr_head)
            {
                ptr = ptr->next;
                head = ptr;
                pre->next = head;
            }
            else
            {
                pre->next = ptr->next;
                ptr = pre->next;
            }
            nptr->next = NULL;
        }
        else
        {
            if (ptr_head)
            {
                ptr_head = false;
            }
            pre = ptr;
            ptr = ptr->next;
        }
    }
    pre->next = nhead;

    if (head == NULL)
        head = nhead;
    return head;
}