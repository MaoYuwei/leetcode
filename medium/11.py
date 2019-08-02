# Container With Most Water

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ret = 0
        i = 0
        j = len(height)-1
        while i<j:
            s = (j-i)*min(height[i], height[j])
            if s > ret:
                ret = s
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return ret
