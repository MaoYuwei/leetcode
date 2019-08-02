class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        ret = []
        self.recursive([-1]*n, 0, [], ret)
        return ret



    def recursive(self, nums, index, path, ret):
        if index==len(nums):
            ret.append(path)
            return

        for i in xrange(len(nums)):
            nums[index]=i
            if self.isValid(nums, index):
                temp = '.' * len(nums)
                self.recursive(nums, index+1, path+[temp[:i]+'Q'+temp[i+1:]], ret)


    def isValid(self, nums, index):
        for i in xrange(index):
            if abs(nums[i]-nums[index])==index-i or nums[i]==nums[index]:
                return False
        return True

if __name__ == '__main__':
    solution = Solution()
    print solution.solveNQueens(8)