# Regular Expression Matching
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # if len(s) == 0 and len(p) == 0:
        #     return True
        # elif len(s) > 0 and len(p) == 0:
        #     return False
        #
        # elif len(p) > 1 and p[1] == '*':
        #     if len(s) > 0 and (s[0] == p[0] or p[0] == '.'):
        #         return self.isMatch(s[1:], p[2:]) or self.isMatch(s[1:], p) or self.isMatch(s, p[2:])
        #     else:
        #         return self.isMatch(s, p[2:])
        #
        # elif len(s) > 0 and len(p) > 0 and (s[0] == p[0] or p[0] == '.'):
        #     return self.isMatch(s[1:], p[1:])
        #
        # return False

        # dynamic programming

        dp = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]
        dp[0][0] = True
        for i in range(1, len(p)):
            if p[i] == '*':
                dp[i + 1][0] = dp[i - 1][0]
        for i in range(len(p)):
            for j in range(len(s)):
                if p[i] == '*':
                    if p[i-1] == s[j] or p[i-1] == '.':
                        dp[i+1][j+1] = dp[i-1][j+1] or dp[i][j+1] or dp[i+1][j]
                    else:
                        dp[i+1][j+1] = dp[i-1][j+1] or dp[i][j+1]
                elif p[i] == s[j] or p[i] == '.':
                    dp[i+1][j+1] = dp[i][j]
        return dp[-1][-1]
