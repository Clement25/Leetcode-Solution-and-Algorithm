# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 11:47:40 2018

@author: DELL
"""


class Solution:
    def isValid(self, s):
        dic = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for c in s:
            if len(stack) == 0:
                stack.append(c)
            elif stack[-1] in [')', ']', '}']:
                return False
            elif c == dic[stack[-1]]:
                stack.pop()
            else:
                stack.append(c)
        if len(stack) == 0:
            return True
        else:
            return False


def main():
    s = '[]{}()'
    s1 = "([)]"
    s2 = "[]}"
    key = Solution()
    print(s1[1:3])
    print(key.isValid(s))
    print(key.isValid(s2))


if __name__ == '__main__':
    main()