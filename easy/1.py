
# two sum
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            x = target - nums[i]
            for j in range(i+1, len(nums)):
                if nums[j] == x:
                    return [i,j]
        return []

if __name__ == '__main__':
    solution = Solution()
    print solution.twoSum([0,4,3,0], 0)