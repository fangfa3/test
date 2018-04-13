# 题目描述
# 我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。
# 请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，
# 总共有多少种方法？

# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        result = list()
        for i in range(number+1):
        	if i == 0:
        		result.append(0)
        		continue
        	if i == 1:
        		result.append(1)
        		continue
        	if i == 2:
        		result.append(2)
        		continue
        	result.append(result[i-1] + result[i-2])
        return result[number]

S = Solution()
print(S.rectCover(5))