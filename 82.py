# Definition for singly-linked list.
# add a new head
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
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        h = ListNode(-1)
        h.next = head
        head = h

        cur = head
        repeat = False
        while cur.next:
            while cur.next.next and cur.next.next.val == cur.next.val:
                cur.next = cur.next.next
                repeat = True
            if repeat == True:
                cur.next = cur.next.next
                repeat = False
            else:
                cur=cur.next

        return head.next

if __name__ == '__main__':
    solution = Solution()
    li = Li([0,0])
    li.printL(li.returnHead())
    print
    h = solution.deleteDuplicates(li.returnHead())
    li.printL(h)