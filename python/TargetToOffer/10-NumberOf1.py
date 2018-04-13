# 题目描述
# 输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。

# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        count = 0
        diff1 = 1
        for i in range(32):
        	if n & diff1:
        		count += 1
        	diff1 = diff1 << 1
        return count 

S = Solution()
print(S.NumberOf1(-7))