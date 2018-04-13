# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        result = ''
        for character in s:
        	if character == ' ':
        		result += '%20'
        	else: result += character
        return result

S = Solution()
print(S.replaceSpace('We are happy.'))