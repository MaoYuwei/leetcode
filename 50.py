class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        flag = 1
        ret = 1
        if n<0:
            flag = 0

        n = abs(n)
        while n>0:
            if n&1 == 1:
                ret = ret*x

            x = x*x
            n>>=1

        if flag == 0:
            ret = 1/float(ret)

        return ret


if __name__ == '__main__':
    solution = Solution()
    print solution.myPow(2,-2)

