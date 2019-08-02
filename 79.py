class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if len(word)==0:
            return False
        m = len(board)
        n = len(board[0])
        mark = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if board[i][j]==word[0]:
                    mark[i][j]=1
                    if self.recursive(board, mark, word[1:], i, j, m, n):
                        return True
                    else:
                        mark[i][j]=0
        return False


    def recursive(self, board, mark, word, i, j, m, n):
        if len(word)==0:
            return True
        if len(word)==1:
            if i>0 and mark[i-1][j]==0 and board[i-1][j]==word[0]:
                return True
            if i<m-1 and mark[i+1][j]==0 and board[i+1][j]==word[0]:
                return True
            if j>0 and mark[i][j-1]==0 and board[i][j-1]==word[0]:
                return True
            if j<n-1 and mark[i][j+1]==0 and board[i][j+1]==word[0]:
                return True
            return False
        flag = False
        if i > 0 and mark[i - 1][j] == 0 and board[i - 1][j] == word[0]:
            mark[i-1][j]=1
            flag = self.recursive(board, mark, word[1:], i-1, j, m, n)
            if flag == True:
                return flag
            else:
                mark[i - 1][j] = 0
        if i < m - 1 and mark[i + 1][j] == 0 and board[i + 1][j] == word[0]:
            mark[i + 1][j] = 1
            flag = self.recursive(board, mark, word[1:], i + 1, j, m, n)
            if flag == True:
                return flag
            else:
                mark[i + 1][j] = 0
        if j > 0 and mark[i][j - 1] == 0 and board[i][j - 1] == word[0]:
            mark[i][j-1] = 1
            flag = self.recursive(board, mark, word[1:], i, j-1, m, n)
            if flag == True:
                return flag
            else:
                mark[i][j - 1] = 0
        if j < n - 1 and mark[i][j + 1] == 0 and board[i][j + 1] == word[0]:
            mark[i][j+1] = 1
            flag = self.recursive(board, mark, word[1:], i, j+1, m, n)
            if flag == True:
                return flag
            else:
                mark[i][j + 1] = 0
        return flag

if __name__ == '__main__':
    solution = Solution()
    print solution.exist([["C","A","A"],["A","A","A"],["B","C","D"]],
"AAB")