class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        try:
            s = float(s)
            return True
        except:
            return False



if __name__ == '__main__':
    solution = Solution()
    print solution.isNumber('e')