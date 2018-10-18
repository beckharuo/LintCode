#!/usr/bin/python3
# -- coding: utf-8 --


class Solution:
    """
    设计一个算法，计算出n阶乘中尾部零的个数
    Write an algorithm which computes the number of trailing zeros in n factorial.
    样例
    11! = 39916800，因此应该返回 2
    挑战
    O(logN)的时间复杂度
    @param: n: An integer
    @return: An integer, denote the number of trailing zeros in n!
    """
    def trailingZeros(self, n):
        # write your code here, try to do it without arithmetic operators.
        num = 0
        while n:
            num = num + n//5
            n = n // 5
        return num


solution = Solution()
print(solution.trailingZeros(11))
