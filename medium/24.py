# Swap Nodes in Pairs

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head

        p = head
        q = p.next
        q.next = self.swapPairs(q.next)
        p.next = q.next
        q.next = p
        return q
