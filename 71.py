class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path = path.split('/')
        # print path
        stack = []
        for p in path:
            if len(p)>0:
                if p not in ['.', '..']:
                    stack.append(p)
                elif p == '..' and len(stack)>0:
                    stack.pop()
        # print stack
        if len(stack)>1:
            return '/'+ '/'.join(stack)
        elif len(stack)>0:
            return '/'+stack[0]
        return '/'
if __name__ == '__main__':
    solution = Solution()
    print solution.simplifyPath("/../")