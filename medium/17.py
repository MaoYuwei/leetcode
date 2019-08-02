# Letter Combinations of a Phone Number

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        dic = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno',
               '7':'pqrs','8':'tuv', '9':'wxyz'}
        ret = ['']
        for digit in digits:
            result = []
            while len(ret) > 0:
                x = ret.pop()
                for w in dic[digit]:
                    result.append(x+w)
            ret = result
        return ret

if __name__ == '__main__':
    solution = Solution()
    print solution.letterCombinations('23')



