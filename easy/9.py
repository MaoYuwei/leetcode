# Palindrome Number

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        r = 0
        bef = x
        if x < 0:
            return False
        while x > 0:
            r *= 10
            r += x%10
            x/=10
        if bef == r:
            return True
        return False

