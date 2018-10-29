#!/usr/bin/python3
# -- coding: utf-8 --


class Solution:
    """
     __|   _ \
     _|    __/    __ \    __ \
          _ \_  \____/  \____/
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
        num = 0
        for i in range(n+1):
            if i == k:
                num += 1
            else:
                while i >= 1:
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
        # 最终答案，超过99%的人
        # 利用数学解法
        # 最简单的逻辑：
        # 当k不为0时
        # 从1至10，在它们的个位数中，任意k都出现了1次。
        # 从1至100，在它们的十位数中，任意k都出现了10次。
        # 从1至1000，在它们的百位数中，任意k都出现了100次。
        # 总结出来的方法：
        # 1.取第i位左边的数字，乘以10的i-1次幂，得到基础值a。
        # 2.取第i位数次，计算修正值：
        # 如果大于k，则结果为a + 10的i - 1次幂；
        # 如果小于k，则结果为a；
        # 如果等于k，则取第i位右边数字，设为b，最后结果为a + b + 1。
        # write your code here
        result = 0
        i = 1
        right = 0
        if k == 0 and n == 0:
            return 1
        # 如果n长度为两位数，并且k为0时，n=0到9十位数的0会被当做重复值，所以删掉
        if 10 <= n < 100 and k == 0:
            result -= 10

        while n >= 1:
            s = n % 10
            n = n // 10

            a = n*(10**(i-1))
            if s > k:
                a += 10**(i-1)
            elif s == k:
                a += right+1
            elif s < k:
                pass

            result += a
            right += s*(10**(i-1))
            i += 1

        return result


solution = Solution()
print(solution.digitCountsByViolence(3, 1284))
print(solution.digitCounts(1, 5))
print(solution.digitCounts(0, 0))
print(solution.digitCounts(1, 1))
