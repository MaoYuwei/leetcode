# Median of Two Sorted Arrays

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        l = nums1 + nums2
        l = sorted(l)
        length = len(l)
        if length%2 == 0:
            return (l[length/2-1] + l[length/2])/2.0
        else:
            return l[length/2]

        
