# 输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
# 使得所有的奇数位于数组的前半部分，所有的偶数位于位于数组的后半部分，
# 并保证奇数和奇数，偶数和偶数之间的相对位置不变。

# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        i = 1
        while i <= len(array) - 1:
        	if array[i] & 1 and not array[i-1] & 1:
        		j = i - 1
        		temp = array[i]
        		while not array[j] & 1 :
        			array[j+1] =array[j]
        			j -= 1
        		array[j+1] = temp
        	i += 1
        return array

if __name__ == '__main__':
	s = Solution()
	print(s.reOrderArray([1, 3, 4, 6, 7, 2, 8, 5, 9]))
