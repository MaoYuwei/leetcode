# Generate Parentheses

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if not n or n == 0:
            return None
        ret = []
        ret = self.S(n, n, ret, '')
        return ret
    def S(self, left, right, ret, string):
        if left == 0 and right == 0:
            ret.append(string)
            return ret
        if right < left:
            return ret
        if left > 0:
            ret = self.S(left-1, right, ret, string+'(')
        if right > 0:
            ret = self.S(left, right-1, ret, string+')')
        return ret

if __name__ == '__main__':
    solution = Solution()
    print solution.generateParenthesis(3)