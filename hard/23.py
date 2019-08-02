# Merge k Sorted Lists
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        import heapq

        heap = []
        for i in lists:
            if i:
                heap.append((i.val, i))

        heapq.heapify(heap)

        p = head = ListNode(0)
        while heap:
            v, x = heap[0]
            p.next = x
            p = p.next
            if x.next:
                heapq.heapreplace(heap, (x.next.val, x.next))
            else:
                heapq.heappop(heap)
        return head.next











