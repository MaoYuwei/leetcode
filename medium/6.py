#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ZigZag Conversion

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        matrix = []
        for i in range(numRows):
            matrix.append([])
        i = 0
        row = 0
        while i < len(s):
            if row == 0:
                while row < numRows:
                    if i >= len(s):
                        break
                    matrix[row].append(s[i])
                    i += 1
                    row += 1
                row -= 2
            else:
                if i >= len(s):
                    break
                matrix[row].append(s[i])
                i += 1
                row -=1

        s = ''
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                s += matrix[i][j]
        return s


if __name__ == '__main__':
    solution = Solution()
    print solution.convert('ABC', 1)