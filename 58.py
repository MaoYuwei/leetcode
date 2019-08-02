class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0
        s = s.split()
        if len(s)==0:
            return 0
        return len(s[-1])

if __name__ == '__main__':
    solution = Solution()
    print solution.lengthOfLastWord("      ")