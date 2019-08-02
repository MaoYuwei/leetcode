
from collections import defaultdict

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        char_need = defaultdict(int)
        print char_need


if __name__ == '__main__':
    solution = Solution()
    print solution.minWindow("ADOBECODEBANC",
"ABC")