class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        left = 0
        right = n-1
        top = 0
        bottom = n-1
        num = 1
        while left<right and top<bottom:
            for i in range(left, right):
                matrix[top][i]=num
                num+=1
            # print matrix
            for i in range(top, bottom):
                matrix[i][right]=num
                num+=1
            # print matrix
            for i in range(right, left, -1):
                matrix[bottom][i]=num
                num+=1
            # print matrix
            for i in range(bottom, top, -1):
                matrix[i][left]=num
                num += 1
            left+=1
            right-=1
            top+=1
            bottom-=1
        if left == right and top == bottom:
            matrix[top][left] = num
        return matrix

if __name__ == '__main__':
    solution = Solution()
    print solution.generateMatrix(3)