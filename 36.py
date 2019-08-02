# 36. Valid Sudoku

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        row = [[] for _ in range(9)]
        column = [[] for _ in range(9)]
        subboxes = [[] for _ in range(9)]
        for i in range(len(board)):
            for j in range(len(board[i])):
                x = board[i][j]
                if x.isdigit():
                    x = int(x)

                    if x in row[i]:
                        return False
                    row[i].append(x)

                    if x in column[j]:
                        return False
                    column[j].append(x)

                    snum = i/3*3+j/3
                    if x in subboxes[snum]:
                        return False
                    subboxes[snum].append(x)

        return True



if __name__ == '__main__':
    solution = Solution()
    print solution.isValidSudoku([
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
])