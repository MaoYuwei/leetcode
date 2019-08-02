# Valid Parentheses

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = ['(', '[', '{']
        right = [')', ']', '}']
        stack = []
        for i in s:
            if i in left:
                stack.append(i)
            elif i in right:
                if len(stack) == 0:
                    return False
                x = stack.pop()
                if left.index(x) != right.index(i):
                    return False
        if len(stack) == 0:
            return True
        return False

if __name__ == '__main__':
    solution = Solution()
    print solution.isValid("()[]{}")
