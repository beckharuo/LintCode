#!/usr/bin/python3
# -- coding: utf-8 --


class Solution:
    """
    计算数字k在0到n中的出现的次数，k可能是0~9的一个值
    Count the number of k's between 0 and n. k can be 0 - 9.
    样例
    例如n=12，k=1，在 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]，我们发现1出现了5次 (1, 10, 11, 12)
    @param k: An integer
    @param n: An integer
    @return: An integer denote the count of digit k in 1..n
    """
    def digitCountsByViolence(self, k, n):
        #遍历一遍，计算每个值k出现的次数
        # write your code here
        print(k, n)
        num = 0
        for i in range(n+1):
            if i == k:
                num += 1
            else:
                while(i >= 1):
                    res = i % 10
                    i = i//10
                    if res == k:
                        num += 1
        return num

    def digitCountsByheat(self, k, n):
        # 利用系统函数作弊了，遍历一遍将所有值拼为字符串，然后用系统函数计算
        # write your code here
        nums = [str(i) for i in range(n + 1)]
        s = ''.join(nums)
        return s.count(str(k))

    def digitCounts(self, k, n):
        result = 0
        return result


solution = Solution()
print(solution.digitCountsByViolence(1, 100))
print(solution.digit(1, 1000))
