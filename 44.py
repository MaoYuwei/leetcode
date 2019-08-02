class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        si, pi, sj, pj = 0,0,-1,-1
        while si<len(s):
            if pi<len(p) and (s[si]==p[pi] or p[pi]=='?'):
                pi+=1
                si+=1
            elif pi<len(p) and p[pi]=='*':
                pi += 1
                pj = pi
                sj = si
            elif pj>=0:
                sj += 1
                si = sj
                pi = pj
            else:
                return False

        while pi<len(p) and p[pi] == '*':
            pi += 1

        return pi == len(p)

if __name__ == '__main__':
    solution = Solution()
    print solution.isMatch("", "*")