#  Integer to Roman

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        s = ''
        if num >= 1000:
            s += 'M'*(num/1000)
            num %= 1000
        if num >= 900:
            s += 'CM'
            num -= 900
        if num >= 500:
            s += 'D'
            num -= 500
        if num >= 400:
            s += 'CD'
            num -= 400
        if num >= 100:
            s += 'C'*(num/100)
            num %= 100
        if num >= 90:
            s += 'XC'
            num -= 90
        if num >= 50:
            s += 'L'
            num -= 50
        if num >= 40:
            s += 'XL'
            num -= 40
        if num >= 10:
            s += 'X'*(num/10)
            num %= 10
        if num >= 9:
            s += 'IX'
            num -= 9
        if num >= 5:
            s += 'V'
            num -= 5
        if num >= 4:
            s += 'IV'
            num -= 4
        if num >= 1:
            s += 'I' * num
        return s

if __name__ == '__main__':

    solution = Solution()
    print solution.intToRoman(1994)