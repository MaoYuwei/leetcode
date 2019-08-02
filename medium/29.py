# Divide Two Integers

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        ret = 0
        a = abs(dividend)
        b = abs(divisor)
        while a >= b:
            count = 1
            sum = b
            while sum + sum < a:
                sum += sum
                count += count
            ret += count
            a -= sum

        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
              ret = -ret

        return min(max(-2147483648, ret), 2147483647)




