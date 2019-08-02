class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums)==1:
            return nums[0]
        current = nums[0]
        m = current
        for i in xrange(1, len(nums)):
            if current < 0:
                current = 0
            current += nums[i]
            m = max(current, m)
        return m

if __name__ == '__main__':
    solution = Solution()
    print solution.maxSubArray([1,2])