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
        if len(s) <= 0:
            return 0
        wordpos = {}
        ret = 0
        left = 0
        for i in range(len(s)):
            if s[i] in wordpos.keys() and left <= wordpos[s[i]]:
                left = wordpos[s[i]] + 1
            else:
                result = i - left + 1
                if result > ret:
                    ret = result
            wordpos[s[i]] = i
        return ret

if __name__ == '__main__':
    solution = Solution()
    s = 'abcabcbb'
    # s = 'qwnfenpglqdq'
    r = solution.lengthOfLongestSubstring(s)
    print r
