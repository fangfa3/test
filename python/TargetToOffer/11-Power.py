# 题目描述
# 给定一个double类型的浮点数base和int类型的整数exponent。
# 求base的exponent次方。

# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        tem  = exponent
        if exponent == 0:
        	return 1
        if exponent < 0:
        	if base == 0:
        		return False
        	tem = -exponent
        result = 1
        for i in range(tem):
        	result *= base
        if exponent < 0:
        	result = 1/result
        return result


S = Solution()
print(S.Power(2,-3))