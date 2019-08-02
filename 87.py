from collections import defaultdict

class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        count1 = defaultdict(int)
        count2 = defaultdict(int)
        count1[1]=1
        count2[1]+=0
        print count1
        print count2

if __name__ == '__main__':
    solution = Solution()
    print solution.isScramble(s1 = "great", s2 = "rgeat")
