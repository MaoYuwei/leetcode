class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        ret = []
        if len(intervals)==0:
            return ret

        intervals.sort(key=lambda x:x[0])

        begin = intervals[0][0]
        end = intervals[0][1]
        if len(intervals)==1:
            return [[begin, end]]

        for i in xrange(1, len(intervals)):
            if intervals[i][0]<=end:
                end = max(intervals[i][1], end)
            else:
                ret.append([begin, end])
                begin = intervals[i][0]
                end = intervals[i][1]
        ret.append([begin, end])
        return ret


if __name__ == '__main__':
    solution = Solution()
    print solution.merge([[1,4],[2,3]])