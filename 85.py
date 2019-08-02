class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        ret = 0

        col = len(matrix[0])
        height = [0 for _ in range(col+1)]

        for i in range(len(matrix)):
            for j in range(col):
                if matrix[i][j]=='0':
                    height[j]=0
                else:
                    height[j]+=1
            stack = [-1]
            for k in range(col+1):
                while height[stack[-1]]>height[k]:
                    h = height[stack.pop()]
                    w = k-stack[-1]-1
                    ret = max(ret, h*w)
                stack.append(k)
        return ret

if __name__ == '__main__':
    solution = Solution()
    print solution.maximalRectangle([
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
])