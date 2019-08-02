class Solution(object):

    def dfs(self, candidates, target, index, path, ret):
        if target < 0:
            return

        elif target == 0:
            ret.append(path)
            return

        for i in xrange(index, len(candidates)):
            if i != index and (candidates[i]==candidates[i-1]):
                continue
            # why use path+[] instead of path.append()
            self.dfs(candidates, target-candidates[i], i+1, path+[candidates[i]], ret)

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        ret = []
        # why ret global?
        candidates.sort()
        self.dfs(candidates, target, 0, [], ret)
        return ret

if __name__ == '__main__':
    solution = Solution()
    print solution.combinationSum([10,1,2,7,6,1,5],8)