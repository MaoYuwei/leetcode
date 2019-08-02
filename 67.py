class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i = len(a)-1
        j = len(b)-1
        ret = []
        flag = 0
        while i>=0 and j>=0:
            s = int(a[i])+int(b[j])+flag
            if s>1:
                s = s%2
                flag = 1
            else:
                flag=0
            ret.append(s)
            i-=1
            j-=1

        while i>=0:
            s = int(a[i])+flag
            if s > 1:
                s = s % 2
                flag = 1
            else:
                flag=0
            ret.append(s)
            i -= 1

        while j>=0:
            s = int(b[j])+flag
            if s > 1:
                s = s % 2
                flag = 1
            else:
                flag=0
            ret.append(s)
            j -= 1

        if flag > 0:
            ret.append(flag)

        ret.reverse()
        ret = map(lambda x:str(x), ret)
        return ''.join(ret)

if __name__ == '__main__':
    solution = Solution()
    print solution.addBinary('1010', '1011')