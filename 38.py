class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n==1:
            return str(1)

        bef = ['1']
        for i in range(1,n):
            if len(bef)==1:
                bef = [str(1), bef[0]]
            else:
                x = bef[0]
                count = 1
                now = []
                for j in range(1, len(bef)):
                    if bef[j]==x:
                        count += 1
                    else:
                        now.append(str(count))
                        now.append(x)
                        x = bef[j]
                        count = 1
                now.append(str(count))
                now.append(x)
                bef = now

        return str(''.join(bef))

if __name__ == '__main__':
    solution = Solution()
    print solution.countAndSay(1)
