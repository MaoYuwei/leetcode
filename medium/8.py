# String to Integer (atoi)

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """

        s = str.strip(' ')
        if len(s) == 0:
            return 0
        if not s[0].isdigit() and s[0] != '-' and s[0] != '+':
            return 0
        r = 0
        i = 0
        flag = 0
        if s[0] == '-' or s[0] == '+':
            i += 1
            if s[0] == '-':
                flag = 1
        if len(s) > 1 and (s[1] == '-' or s[1] == '+'):
            return 0
        while i < len(s):
            if s[i].isdigit():
                r *= 10
                r += int(s[i])
                mark = 1
            # elif s[i].isdigit() and mark == 1:
            #     r += 10**(-q)*int(s[i])
            #     q += 1
            else:
                break
            i += 1

        if flag == 1:
            r = -r

        if r < -2**31:
            return -2**31
        if r > 2**31-1:
            return 2**31-1
        return r

if __name__ == '__main__':
    solution = Solution()
    print solution.myAtoi('  -0012a42')