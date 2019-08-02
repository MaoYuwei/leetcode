class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        i = 0
        while i < len(nums):
            if nums[i]==target:
                return True
            i += 1
        return False

if __name__ == '__main__':
    solution = Solution()
    print solution.search(nums = [2,5,6,0,0,1,2], target = 0)