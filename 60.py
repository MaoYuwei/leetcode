import math
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        k -= 1
        ret = []
        nums = range(1,n+1)
        while n>0:
            n -= 1
            i, k = divmod(k, math.factorial(n))
            ret.append(nums[i])
            nums.remove(nums[i])

        ret = map(lambda x:str(x), ret)
        return ''.join(ret)



if __name__ == '__main__':
    solution = Solution()
    print solution.getPermutation(3,3)