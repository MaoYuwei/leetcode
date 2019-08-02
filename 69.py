import math
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        return int(math.sqrt(x))

if __name__ == '__main__':
    solution = Solution()
    print solution.mySqrt(4)