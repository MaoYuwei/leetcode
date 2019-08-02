class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        l = len(matrix[0])
        for i in range(l):
            for j in range(l-i):
                matrix[i][j], matrix[l-j-1][l-i-1]=matrix[l-j-1][l-i-1], matrix[i][j]


        for i in range(l/2):
            for j in range(l):
                matrix[i][j], matrix[l-i-1][j] = matrix[l-i-1][j], matrix[i][j]
        return matrix

if __name__ == '__main__':
    solution = Solution()
    print solution.rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])



