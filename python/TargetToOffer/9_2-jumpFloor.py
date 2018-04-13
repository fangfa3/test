# 题目描述
# 一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法。

# 后面补充了如何跳

# -*- coding:utf-8 -*-
import copy

class Solution:
    def jumpFloor(self, number):
        # # fangfa1:
        jumpMethods = []
        for i in range(1,number+1):
        	if i == 1:
        		jumpMethods.append(1)
        		continue
        	if i == 2:
        		jumpMethods.append(2)
        		continue
        	jumpMethods.append(jumpMethods[i-2]+jumpMethods[i-3])
        return jumpMethods[number-1]

        # #fangfa2:
        # if number == 1:
        # 	return 1
        # if number == 2:
        # 	return 2
        # return self.jumpFloor(number-1) + self.jumpFloor(number-2)

    def HowToJump(self, number):
    	jumpWay = list()
    	self.Permutation(jumpWay,number)

    def Permutation(self, jumpWay, number):
    	if number == 0:
    		print(jumpWay)
    		return
    	if number >= 1:
    		temp1 = copy.copy(jumpWay)
    		temp1.append(1)
    		self.Permutation(temp1, number-1)
    	if number >= 2:
    		temp2 = copy.copy(jumpWay)
    		temp2.append(2)
    		self.Permutation(temp2, number-2)


S = Solution()
print(S.jumpFloor(10))
S.HowToJump(10)