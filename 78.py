class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = [[]]
        for i in range(len(nums)):
            for j in range(len(ret)):
                cur = ret[j]+[nums[i]]
                # print cur
                ret += [cur]
        return ret



if __name__ == '__main__':
    solution = Solution()
    print solution.subsets([1,2,3])