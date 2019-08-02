class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1)
        n = len(word2)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(n+1):
            dp[0][i]=i
        for j in range(m+1):
            dp[j][0]=j
        for i in range(1, m+1):
            for j in range(1, n+1):
                flag = 0
                if word1[i-1] != word2[j-1]:
                    flag = 1
                dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+flag)


        # print dp
        return dp[-1][-1]

if __name__ == '__main__':
    solution = Solution()
    print solution.minDistance(word1 = "intention", word2 = "execution")