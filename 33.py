# 33. Search in Rotated Sorted Array
# Medium
# Suppose an array sorted in ascending order is rotated
# at some pivot unknown to you beforehand.
# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
# You are given a target value to search. If found in the array
# return its index, otherwise return -1.
# You may assume no duplicate exists in the array.
# Your algorithm's runtime complexity must be in the order of O(log n).

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if len(nums)==0:
            return -1

        if nums[0] == target:
            return 0

        if len(nums)==1:
            return -1

        elif nums[0] < target:
            i = 1
            while i < len(nums) - 1 and nums[i] < nums[i + 1]:
                if target == nums[i]:
                    return i
                i += 1
            if target == nums[i]:
                return i
            return -1

        else:
            i = len(nums) - 1
            while i > 0 and nums[i] > nums[i - 1]:
                if target == nums[i]:
                    return i
                i -= 1
            if target == nums[i]:
                return i
            return -1


if __name__ == '__main__':
    solution = Solution()
    print solution.search([4, 5, 6, 7, 0, 1, 2], 0)
