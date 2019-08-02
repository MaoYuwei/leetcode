# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Lists(object):
    def __init__(self, l):
        if len(l)==0:
            self.head = None
        else:
            self.head = ListNode(l[0])
            if len(l) > 0:
                cur = self.head
                for i in xrange(1, len(l)):
                    cur.next = ListNode(l[i])
                    cur = cur.next

    def returnHead(self):
        return self.head

    def showList(self):
        cur = self.head
        if not cur:
            return None
        while cur.next:
            print cur.val, '->',
            cur = cur.next
        print cur.val

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        n = 1
        cur = head
        if not cur:
            return None
        while cur.next:
            cur = cur.next
            n += 1
        n = n - k%n
        # print n
        cur.next = head
        cur = head
        # print cur.val
        while n>1 and cur.next:
            cur = cur.next
            n -= 1
        # print cur.val
        head = cur.next
        cur.next = None
        return head

if __name__ == '__main__':
    li = Lists([1,2,3,4,5])
    li.showList()
    solution = Solution()
    test = li.returnHead()
    l = solution.rotateRight(li.returnHead(), 1)
    cur = l
    if cur:
        while cur.next:
            print cur.val, '->',
            cur = cur.next
        print cur.val







