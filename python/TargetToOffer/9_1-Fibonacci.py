# 题目描述
# 大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项。
# n<=39

# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        result = [0, 1]
        for i in range(0, n+1):
        	if i ==0 or i == 1:
        		continue
        	result.append(result[i-1] + result[i-2])
        return result[n]

S = Solution()
print(S.Fibonacci(37))
