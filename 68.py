class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        ret = []
        cur = []
        for i, word in enumerate(words):
            if len(' '.join(cur))+len(word)<=maxWidth-1:
                cur.append(word)
            else:
                # print cur
                spaces = maxWidth-len(''.join(cur))-len(cur)+1
                if len(cur)>0:
                    if len(cur) > 1:
                        a, b = divmod(spaces, len(cur)-1)

                        for i in range(len(cur)-1):
                            cur[i] += ' '*a
                            if b > 0:
                                cur[i] += ' '
                                b -= 1
                        ret.append(' '.join(cur))
                    else:
                        ret.append(cur[0]+' '*(maxWidth-len(cur[0])))
                cur = [word]
        s = ' '.join(cur)
        ret.append(s+' '*(maxWidth-len(s)))
        # for i in ret:
        #     print i, len(i)
        return ret

if __name__ == '__main__':
    solution = Solution()
    print solution.fullJustify(["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
,20)