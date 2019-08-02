# Substring with Concatenation of All Words

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if s == '' or len(words) == 0:
            return []
        l = len(words[0])
        dicw = {}
        for w in words:
            if w in dicw.keys():
                dicw[w] += 1
            else:
                dicw[w] = 1


        ret = []
        lw = len(words)
        for i in range(len(s)-l*lw+1):

            dics = {}
            k = i
            while k < i+l*lw:
                word = s[k:k+l]
                if word not in dicw.keys():
                    break
                if word not in dics.keys():
                    dics[word] = 1
                else:
                    dics[word] += 1
                if dics[word] > dicw[word]:
                    break
                k += l
            if k == i+l*lw:
                ret.append(i)

        return ret

if __name__ == '__main__':
    solution = Solution()
    print solution.findSubstring("barfoothefoobarman", ["foo","bar"])




