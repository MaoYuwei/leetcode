# Reverse Nodes in k-Group

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k <= 1 or not head or not head.next:
            return head

        mark = k
        p = head
        q = p.next
        while k > 2 and q.next:
            p = p.next
            q = p.next
            k -= 1

        if k > 2:
            return head

        x = self.reverseKGroup(q.next, mark)
        p.next = None
        q.next = self.reverseKGroup(head, mark-1)
        head = q
        while q.next:
            q = q.next
        q.next = x
        return head