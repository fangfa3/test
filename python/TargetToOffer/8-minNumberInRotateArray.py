# 把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
#  输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。 
#  例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。 
#  NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。

# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if not rotateArray:
        	return 0
        begin = 0
        end = len(rotateArray) - 1
        if rotateArray[begin] < rotateArray[end]:
        	return rotateArray[begin]
        while rotateArray[begin] >= rotateArray[end]:
        	if end - begin <=1:
        		break
        	mid = int((begin + end)/2)
        	if rotateArray[mid] >= rotateArray[begin]:
        		begin = mid
        	if rotateArray[mid] < rotateArray[begin]:
        		end = mid
        	if rotateArray[mid] == rotateArray[begin] and rotateArray[mid] == rotateArray[end]:
        		return min(rotateArray)

        return rotateArray[end]

S = Solution()
A = [3, 4, 5, 6, 7, 2]
B = [1, 1, 1, 1, 0, 1]
C = [1, 2, 3, 4, 5 ,6]
print(S.minNumberInRotateArray(A))