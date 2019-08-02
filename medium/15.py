# 3Sum

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        ret = []
        i = 0
        while i < len(nums) and nums[i] <= 0:
            if i > 0 and nums[i] == nums[i-1]:
                i += 1
                continue
            x = -nums[i]
            j = i+1
            k = len(nums)-1
            while j < k and nums[k] >= 0:
                if nums[j]+nums[k] < x:
                    j += 1
                elif nums[j]+nums[k] > x:
                    k -= 1
                else:
                    ret.append([nums[i], nums[j], nums[k]])
                    while j<k and nums[j+1] == nums[j]:
                        j += 1
                    while j<k and nums[k-1] == nums[k]:
                        k -= 1
                    j += 1
                    k -= 1
            i += 1
        return ret

if __name__ == '__main__':
    solution = Solution()
    print solution.threeSum([-1,0,1,2,-1,-4])
