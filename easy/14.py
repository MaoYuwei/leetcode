# Longest Common Prefix

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        ret = strs[0]
        for i in range(1, len(strs)):
            x = strs[i]
            j = 0
            while j < min(len(ret), len(x)) and ret[j] == x[j]:
                j += 1
            if j == 0:
                return ''
            else:
                ret = ret[:j]
        return ret

if __name__ == '__main__':
    solution = Solution()
    print solution.longestCommonPrefix(["flower","flow","flight"])


