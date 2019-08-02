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
        if head == None:
            return None
        cur = head
        repeat = False
        while cur.next:
            while cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next
                repeat = True
            if repeat == True:
                repeat = False
            else:
                cur = cur.next


        return head

if __name__ == '__main__':
    solution = Solution()
    li = Li([1,1,2])
    li.printL(li.returnHead())
    print
    h = solution.deleteDuplicates(li.returnHead())
    li.printL(h)