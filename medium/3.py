#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Given a string, find the length of the longest substring
# without repeating characters.
#
# Examples:
#
# Given "abcabcbb", the answer is "abc", which the length is 3.
#
# Given "bbbbb", the answer is "b", with the length of 1.
#
# Given "pwwkew", the answer is "wke", with the length of 3.
# Note that the answer must be a substring,
# "pwke" is a subsequence and not a substring.

class Solution(object):
    # def issubstring(self,s):
    #     if len(list(s)) == len(set(list(s))):
    #         return True
    #     return False
    #
    # def lengthOfLongestSubstring(self, s):
    #     """
    #     :type s: str
    #     :rtype: int
    #     """
    #     if self.issubstring(s) == False:
    #         return max(self.lengthOfLongestSubstring(s[1:]), self.lengthOfLongestSubstring(s[:-1]))
    #
    #     return len(s)
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        import operator
        if len(s) <= 0:
            return 0
        wordpos = {}
        for i in range(len(s)):
            j = 0
            while i + j < len(s):
                if s[j] != s[i]:
                    break
                j += 1

            if s[i] in wordpos.keys():
                if j+1 > wordpos[s[i]]:
                    wordpos[s[i]] = j+1
            else:
                wordpos[s[i]] = j + 1

        wl = zip(wordpos.keys(), wordpos.values())
        wl = sorted(wl, key=operator.itemgetter(0))
        wl = sorted(wl, key=operator.itemgetter(0))
        print wl
        return ''.join([wl[0][0]]*wl[0][1])

if __name__ == '__main__':
    import sys
    solution = Solution()
    # s = 'abcabcbb'
    # # s = 'qwnfenpglqdq'
    # r = solution.lengthOfLongestSubstring(s)
    # print r
    s = sys.stdin.readline().strip()
    solution.lengthOfLongestSubstring(s)
