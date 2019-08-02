# Next Permutation

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = len(nums)-1
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        i -= 1
        if i == -1:
            self.reverse(nums, 0, len(nums) - 1)
        else:
            j = len(nums) - 1
            while j > i and nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
            print nums
            self.reverse(nums, i+1, len(nums)-1)
            return nums

        return nums

    def reverse(self, l, begin, end):
        while begin < end:
            l[begin], l[end] = l[end], l[begin]
            begin += 1
            end -= 1

if __name__ == '__main__':
    solution = Solution()
    print solution.nextPermutation([1,3,2])


