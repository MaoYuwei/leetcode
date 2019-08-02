# Roman to Integer

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret = 0
        i = 0
        while i < len(s):
            if s[i] == 'M':
                ret += 1000
            elif s[i] == 'D':
                ret += 500
            elif s[i] == 'C':
                if i + 1 < len(s):
                    if s[i+1] == 'D':
                        ret += 400
                        i += 1
                    elif s[i+1] == 'M':
                        ret += 900
                        i += 1
                    else:
                        ret += 100
                else:
                    ret += 100
            elif s[i] == 'L':
                ret += 50
            elif s[i] == 'X':
                if i + 1 < len(s):
                    if s[i+1] == 'L':
                        ret += 40
                        i += 1
                    elif s[i+1] == 'C':
                        ret += 90
                        i += 1
                    else:
                        ret += 10
                else:
                    ret += 10
            elif s[i] == 'V':
                ret += 5
            elif s[i] == 'I':
                if i+1 < len(s):
                    if s[i+1] == 'V':
                        ret += 4
                        i += 1
                    elif s[i+1] == 'X':
                        ret += 9
                        i += 1
                    else:
                        ret += 1
                else:
                    ret += 1
            i += 1
        return ret

if __name__ == '__main__':
    solution = Solution()
    print solution.romanToInt('III')