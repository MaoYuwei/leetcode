# Reverse Integer

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < ((-2)**31) or x > (2**31-1):
            return 0
        r = 0

        if x >= 0:
            while x > 0:
                r *= 10
                r += x%10
                x /= 10

        else:
            x = -x
            while x > 0:
                r *= 10
                r += x%10
                x /= 10
            r = -r

        if r < ((-2)**31) or r > (2**31-1):
            return 0

        return r

if __name__ == '__main__':
    solution = Solution()
    print solution.reverse(123)