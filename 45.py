class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        end = 0
        ret = 0

        while end < len(nums)-1:
            ret += 1
            maxend = end+1
            for i in range(start, end+1):
                if nums[i]+i>=len(nums)-1:
                    return ret
                maxend = max(maxend, nums[i]+i)
            start, end = end+1, maxend
        return ret

if __name__ == '__main__':
    solution = Solution()
    print solution.jump([2,3,1,1,4])




