# Definition for singly-linked list.

# remember add a head node

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Li(object):
    def __init__(self, l):
        self.head = ListNode(l[0])
        cur = self.head
        for i in range(1, len(l)):
            cur.next = ListNode(l[i])
            cur = cur.next

    def returnHead(self):
        return self.head

    def printL(self, head):
        cur = head
        while cur:
            print cur.val,'->',
            cur = cur.next

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        L = ListNode(x-1)
        L.next = head
        head = L
        
        cur = head
        while cur:
            while cur.next and cur.next.val<x:
                cur = cur.next
            if cur.next == None:
                return head.next

            next = cur.next
            while next.next and next.next.val>=x:
                next = next.next
            if next.next == None:
                return head.next
            q = next.next
            next.next = next.next.next
            temp = cur.next
            cur.next = q
            cur = cur.next
            cur.next = temp

        return head.next

if __name__ == '__main__':
    solution = Solution()
    li = Li([2,3,1])
    head = li.returnHead()
    print li.printL(head)
    head = solution.partition(head, 2)
    print li.printL(head)
