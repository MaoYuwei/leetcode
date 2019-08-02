class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.append(0)
        stack = [-1]
        ret = 0
        for i in range(len(heights)):
            while heights[stack[-1]]>heights[i]:
                h = heights[stack.pop()]
                w = i-stack[-1]-1
                ret = max(ret, h*w)

            stack.append(i)
        heights.pop()
        return ret



if __name__ == '__main__':
    solution = Solution()
    print solution.largestRectangleArea([2,1,5,6,2,3])