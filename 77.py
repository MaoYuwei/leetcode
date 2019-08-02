class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        ret = []
        self.recursive(range(1, n+1), k, [], ret)
        return ret

    def recursive(self, l, k, nums, ret):
        if len(nums)==k:
            # print ret
            # nums.sort()
            # print nums

            ret.append(nums+[])
            nums = []
            return
        for i in range(len(l)):
            # print nums
            nums.append(l[i])
            self.recursive(l[i+1:], k, nums, ret)
            nums.pop()

if __name__ == '__main__':
    solution = Solution()
    print solution.combine(4, 2)