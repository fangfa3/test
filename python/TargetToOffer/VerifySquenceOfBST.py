# 题目描述
# 输入一个整数数组，
# 判断该数组是不是某二叉搜索树的后序遍历的结果。
# 如果是则输出Yes,否则输出No。
# 假设输入的数组的任意两个数字都互不相同。

# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence:
        	return False
        if len(sequence) == 1:
        	return True
        root = sequence[-1]
        i = 0
        while sequence[i] < root:
        	i += 1
        for j in sequence[i: -1]:
        	if j < root:
        		return False
        left = True
        right = True
        if len(sequence[0:i]) > 0:
        	left = self.VerifySquenceOfBST(sequence[0:i])
        if len(sequence[i:-1]) > 0:
        	right = self.VerifySquenceOfBST(sequence[i:-1])
        return left and right

if __name__ == '__main__':
	S = Solution()
	a = [7, 4, 6, 5]
	print(S.VerifySquenceOfBST(a))

