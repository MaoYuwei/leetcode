class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        left = []
        right = []
        maxleft = 0
        maxright = 0
        for i in range(len(height)):
            left.append(maxleft)
            maxleft=max(maxleft, height[i])
            right.append(maxright)
            maxright=max(maxright, height[len(height)-1-i])

        right.reverse()
        ret = 0
        for i in range(len(height)):
            h = min(left[i], right[i])
            if h>height[i]:
                ret += h-height[i]


        return ret


if __name__ == '__main__':
    solution = Solution()
    print solution.trap([0,1,0,2,1,0,1,3,2,1,2,1])