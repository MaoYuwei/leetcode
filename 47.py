class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        result = []
        self.get_permuteUnique([], nums, result)
        return result

    def get_permuteUnique(self, current, nums, result):
        if not nums:
            if current not in result:
                result.append(current+[])
            return

        for i in range(len(nums)):
            current.append(nums[i])
            self.get_permuteUnique(current, nums[:i]+nums[i+1:], result)
            current.pop()


if __name__ == '__main__':
    solution = Solution()
    print solution.permuteUnique([1,1,2])