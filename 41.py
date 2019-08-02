class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = 1

        nums.sort()
        index = 0
        while index<len(nums) and nums[index]<=0:
            index+=1

        while index<len(nums):
            if index>0 and nums[index]==nums[index-1]:
                index+=1
                continue
            if nums[index]==x:
                x += 1
                index+=1
            else:
                break

        return x

if __name__ == '__main__':
    solution = Solution()
    print solution.firstMissingPositive([1])