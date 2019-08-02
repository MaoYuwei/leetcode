class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        return nums

if __name__ == '__main__':
    solution = Solution()
    print solution.sortColors([2,0,2,1,1,0])