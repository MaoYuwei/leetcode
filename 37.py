# 37. Sudoku Solver

class Solution(object):
    # def isValid(self, board, row, col, c):
    #     for i in range(9):
    #         if board[row][i]==c:
    #             return False
    #         if board[i][col]==c:
    #             return False
    #         if board[row/3*3+col/3][i]==c:
    #             return False
    #     return True

    def isValid(self, board, x, y):
        # row
        for i in range(9):
            if i != x and board[i][y] == board[x][y]:
                return False
        # col
        for j in range(9):
            if j != y and board[x][j] == board[x][y]:
                return False

        # 3x3 box
        x_st, y_st = 3 * (x / 3), 3 * (y / 3)
        for i in range(x_st, x_st + 3):
            for j in range(y_st, y_st + 3):
                if (i != x or j != y) and board[i][j] == board[x][y]:
                    return False
        return True

    def solve(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j]=='.':
                    for x in '123456789':
                        board[i][j] = x
                        if self.isValid(board, i, j) and self.solve(board):
                            return True
                        board[i][j]='.'
                    return False
        return True


    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        self.solve(board)
        print board

if __name__ == '__main__':
    solution = Solution()

    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."],
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]


    solution.solveSudoku(board)