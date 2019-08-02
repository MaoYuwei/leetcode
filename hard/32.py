# Longest Valid Parentheses

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '':
            return 0
        ret = 0
        stack = []
        last = -1
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if len(stack) == 0:
                    last = i
                else:
                    stack.pop()
                    if len(stack) > 0:
                        ret = max(ret, i-stack[-1])
                    else:
                        ret = max(ret, i-last)
        return ret



if __name__ == '__main__':
    solution = Solution()
    print solution.longestValidParentheses("()")



