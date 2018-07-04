#!/usr/bin/env python
# coding=utf-8

#第十一章 链表

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedList:
    def __init__(self, l):
        self.Head = ListNode(l[0])
        Node = self.Head
        for i in range(1, len(l)):
            Node.next = ListNode(l[i])
            Node = Node.next

    def p(self):
        node = self.Head
        while node:
            print node.val
            node = node.next
        return self.Head

    def deleteDuplication(self, pHead):
        #在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。
        # 例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
        if pHead is None or pHead.next is None:
            return pHead
        elif pHead.val != pHead.next.val:
            pHead.next = self.deleteDuplication(pHead.next)
        else:
            head = pHead.next
            while head.next is not None and head.next.val == pHead.val:
                head = head.next
            if head.next is None:
                return None
            else:
                pHead = self.deleteDuplication(head.next)
        return pHead

    def EntryNodeOfLoop(self, pHead):
        #一个链表中包含环，请找出该链表的环的入口结点。
        p = []
        while pHead:
            if pHead in p:
                return pHead
            p.append(pHead)
            pHead = pHead.next
        return None

    def printListFromTailToHead(self, listNode):
        #输入一个链表，从尾到头打印链表每个节点的值。
        p = []
        pHead = listNode
        while pHead:
            p.insert(0, pHead.val)
            pHead = pHead.next
        return p



def main():
    linkedlist = LinkedList([1,2,3,4,5])
    Head = linkedlist.p()
    print
    # linkedlist.deleteDuplication(Head)
    linkedlist.printListFromTailToHead(Head)
    linkedlist.p()





if __name__ == "__main__":
    main()