#!/usr/bin/env python
# -*- coding: utf-8 -*-

# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order and
# each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero,
# except the number 0 itself.
#
# Example
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# Definition for singly-linked list.

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
            print node.val,
            node = node.next
        print '\n'
        return self.Head


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        mark = 0
        s = l1.val + l2.val
        if s >= 10:
            mark = 1
            s = s - 10
        head = ListNode(s)
        node = head
        l1 = l1.next
        l2 = l2.next

        while l1 and l2:
            s = l1.val + l2.val + mark
            mark = 0
            if s >= 10:
                mark = 1
                s = s - 10
            node.next = ListNode(s)
            node = node.next
            l1 = l1.next
            l2 = l2.next

        if mark == 0:
            if l1:
                node.next = l1
            elif l2:
                node.next = l2
        if mark == 1:
            while l1:
                s = mark + l1.val
                mark = 0
                if s >= 10:
                    mark = 1
                    s = s - 10
                node.next = ListNode(s)
                node = node.next
                l1 = l1.next

            while l2:
                s = mark + l2.val
                mark = 0
                if s >= 10:
                    mark = 1
                    s = s - 10
                node.next = ListNode(s)
                node = node.next
                l2 = l2.next

            if mark == 1:
                node.next = ListNode(mark)
        return head

if __name__ == '__main__':

    l1 = [9,8]
    l1 = LinkedList(l1).p()

    l2 = [1]
    l2 = LinkedList(l2).p()

    solution = Solution()
    l = solution.addTwoNumbers(l1, l2)

    while l:
        print l.val,
        l = l.next
