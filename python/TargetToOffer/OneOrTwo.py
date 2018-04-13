#递归思路：一个数字串，从头开始看，要么是第一个单独为一个，要么是第一个和第二个合并为一个；
#这两种不管选择哪一种之后还会剩下一个数字串，对这个剩下的数字串继续这样的操作。
#当然，每一步都要判断下条件，比如说剩下的字符串长度必须大于2才能将两个合并。最后数字串没有了就输出一个结果。

import copy
class Solution:
	def Find(self, s): #s为输入的数字串
		result = [] #定义一个空列表，方便递归
		self.Permutation(result, s) # 进入递归

	def Permutation(self, result, tr):
		if not tr:  #数字串为空，即代表递归结束，输出对应结果。
			print(result)
			return
		if len(tr) >= 1:  #数字串长度大于1时，将该字符串的第一个单独加入结果列表
			temp1 = copy.copy(result)
			temp1.append(int(tr[0]))
			self.Permutation(temp1, tr[1:]) #对剩下的数字串继续重复
		if len(tr) >= 2:  #数字串长度大于2时，将该字符串的前两个合并加入结果列表
			temp2 = copy.copy(result)
			temp2.append(int(tr[0]+tr[1]))
			self.Permutation(temp2, tr[2:]) #对剩下的数字串继续重复

#测试		
S = Solution()
S.Find('1234')

#结果
#[1, 2, 3, 4]
#[1, 2, 34]
#[1, 23, 4]
#[12, 3, 4]
#[12, 34]