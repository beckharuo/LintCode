#!/usr/bin/python3
# -- coding: utf-8 --
'''
 __|   _ \
 _|    __/
      _ \_
'''
from collections import deque


class Solution(object):

    # @param nestedList a list, each element in the list
    # can be a list or integer, for example [1,2,[1,2]]
    # @return {int[]} a list of integer
    def flatten(self, nestedList):
        output, queue = [], deque([nestedList])
        while queue:
            elements = queue.popleft()
            if isinstance(elements, list):
                for elem in reversed(elements):
                    queue.appendleft(elements.pop())
                print(queue)
            else:
                output.append(elements)
        return output


cl = Solution()

s=cl.flatten([1,[4,[6]]])
ss = cl.flatten([[1,1],2,[1,1]])
print(s)
print(ss)
