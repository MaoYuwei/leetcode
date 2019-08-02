# 3Sum Closest

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        ret = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i+1
            k = len(nums)-1
            while j<k:
                s = nums[i] + nums[j] + nums[k]
                if s == target:
                    return target
                if abs(ret-target) > abs(s-target):
                    ret = s
                if s > target:
                    k -= 1
                if s < target:
                    j += 1

        return ret
