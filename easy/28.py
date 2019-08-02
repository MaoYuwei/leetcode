# Implement strStr()

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack == '' and needle == '':
            return 0
        for i in range(len(haystack)-len(needle)+1):
            j = 0
            k = i
            while k < len(haystack) and j < len(needle) and haystack[k] == needle[j]:
                j += 1
                k += 1
            if j == len(needle):
                return i
        return -1

if __name__ == '__main__':
    solution = Solution()
    print solution.strStr('a', 'a')