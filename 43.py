class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        n1 = 0
        for i in xrange(len(num1)):
            n1+=int(num1[i])*(10**(len(num1)-i-1))

        n2 = 0
        for i in xrange(len(num2)):
            n2 += int(num2[i]) * (10 ** (len(num2) - i - 1))

        return str(n1*n2)

if __name__ == '__main__':
    solution = Solution()
    print solution.multiply('123', '456')