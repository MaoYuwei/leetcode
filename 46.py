class Solution(object):

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.get_permute([], nums, result)
        return result


    def get_permute(self, current, nums, result):
        if not nums:
            result.append(current+[])
            return
        for i in range(len(nums)):
            current.append(nums[i])
            self.get_permute(current, nums[:i]+nums[i+1:], result)
            current.pop()

if __name__ == '__main__':
    solution = Solution()
    print solution.permute([1,2,3])
