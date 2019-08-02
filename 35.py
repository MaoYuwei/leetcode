# 35. Search Insert Position

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums)==0:
            return 0

        i = 0
        while i<len(nums) and nums[i]<=target:
            if nums[i]==target:
                return i
            i += 1
        return i

if __name__ == '__main__':
    solution = Solution()
    print solution.searchInsert([1,3,5,6], 2)