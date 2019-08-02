# 4Sum

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        ret = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                x = target - nums[i] - nums[j]
                k = j + 1
                l = len(nums)-1
                # while l > k and nums[l] > x:
                #     l -= 1
                # while l > k and x > nums[l] + nums[k]:
                #     k += 1
                while k < l:
                    if k < l and x < nums[l] + nums[k]:
                        l -= 1
                    if k < l and x > nums[l] + nums[k]:
                        k += 1
                    if k < l and x == nums[l] + nums[k]:
                        r = [nums[i], nums[j], nums[k], nums[l]]
                        if r not in ret:
                            ret.append(r)
                        l -= 1
        return ret

if __name__ == '__main__':
    solution = Solution()
    print solution.fourSum([1,-2,-5,-4,-3,3,3,5], -11)