class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits = map(lambda x:str(x), digits)
        s = ''.join(digits)
        s = int(s)+1
        s = str(s)
        s = list(s)
        s = map(lambda x:int(x), s)
        return s


if __name__ == '__main__':
    solution = Solution()
    print solution.plusOne([1,2,3])