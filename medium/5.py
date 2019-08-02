#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  Given a string s, find the longest palindromic substring in s.
#  You may assume that the maximum length of s is 1000.

# Example 1:
#
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:
#
# Input: "cbbd"
# Output: "bb"

def Solution(s):
# 遍历每个中心i,向两边扩展比较是否相等， O(n)
    ret = 0
    if len(s) == 0:
        return ''
    if len(s) == 1:
        return s
    for i in range(len(s)):
        # 奇数
        j = 0
        while i-j >= 0 and i+j < len(s):
            if s[i-j] != s[i+j]:
                break
            j += 1
        if 2*j+1 > ret:
            ret = 2*j+1
            rs = s[i-j+1:i+j]

        # 偶数
        j = 0
        while i-j >= 0 and i+j+1 < len(s):
            if s[i-j] != s[i+j+1]:
                break
            j += 1
        if 2*j+2 > ret:
            ret = 2*j+2
            rs = s[i-j+1:i+j+1]

    return rs




if __name__ == '__main__':
    s = 'cbbd'
    print Solution(s)