# 题目描述
# 一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。
# 求该青蛙跳上一个n级的台阶总共有多少种跳法。

# 思路： 用递归的方法考虑问题，得出表达式；
#如果要输出所有跳法，可以使用循环来做，每次在之前的基础上再加跳法。

# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        # write code here
        if number == 1:
        	return 1
        return 2 * self.jumpFloorII(number - 1)
		
S = Solution()
print(S.jumpFloorII(6))