# 34. Find First and Last Position of Element in Sorted Array

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums)==0:
            return [-1, -1]
        if len(nums)==1:
            if target==nums[0]:
                return [0, 0]
            else:
                return [-1, -1]

        begin, end = 0, len(nums)-1
        while begin<end:
            if nums[begin]<target:
                begin+=1
            if nums[end]>target:
                end-=1
            if nums[begin]==target and nums[end]==target:
                return [begin, end]
        if nums[begin]==target:
            return [begin, end]

        return [-1,-1]


if __name__ == '__main__':
    solution = Solution()
    print solution.searchRange([5,7,7,8,8,10],6)