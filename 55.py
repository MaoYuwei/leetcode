class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        if len(nums)<=1:
            return True

        longest = nums[0]
        for i in xrange(0, len(nums)):
            if i>longest:
                return False
            if longest >= len(nums)-1:
                return True
            longest = max(i+nums[i], longest)
        return False



if __name__ == '__main__':
    solution = Solution()
    print solution.canJump([2,3,1,1,4])