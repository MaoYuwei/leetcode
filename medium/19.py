# Remove Nth Node From End of List

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        p = head
        q = head
        while n > 0 and p:
            p = p.next
            n -= 1
        if not p and n > 0:
            return head
        if not p and n == 0:
            return head.next
        while p.next and q.next:
            p = p.next
            q = q.next
        q.next = q.next.next
        return head
