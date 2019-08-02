class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        ret = []
        self.spiral(matrix, ret)
        return ret

    def spiral(self, matrix, ret):
        if len(matrix)==0:
            return
        if len(matrix)==1:
            ret.extend(matrix[0])
            return

        ret.extend(matrix[0])
        matrix.pop(0)

        temp = []
        for i in xrange(len(matrix)):
            if len(matrix[i]) > 0:

                temp.append(matrix[i][-1])
                matrix[i].pop(-1)
        ret.extend(temp)

        if len(matrix[-1])>0:
            matrix[-1].reverse()
            ret.extend(matrix[-1])
            matrix.pop(-1)

        temp = []
        for i in xrange(len(matrix)-1, -1, -1):
            if len(matrix[i])>0:
                temp.append(matrix[i][0])
                matrix[i].pop(0)
        ret.extend(temp)
        self.spiral(matrix, ret)

if __name__ == '__main__':
    solution = Solution()
    print solution.spiralOrder([[7],[9],[6]])