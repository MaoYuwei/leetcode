class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        dict = {}
        for i in range(len(strs)):
            s = strs[i]
            key = ''.join(sorted(s))
            if key in dict.keys():
                dict[key].append(s)
            else:
                dict[key]=[s]

        ret = []
        for k in dict.keys():
            ret.append(dict[k])

        return ret

if __name__ == '__main__':
    solution = Solution()
    print solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])