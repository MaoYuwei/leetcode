class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for i in range(len(nums)):
            if count<2 or nums[count-2]!= nums[i]:
                nums[count]=nums[i]
                count+=1
        return count


if __name__ == '__main__':
    solution = Solution()
    print solution.removeDuplicates([0,0,1,1,1,1,2,3,3])