# 题目描述
# 输入两个单调递增的链表，输出两个链表合成后的链表，
# 当然我们需要合成后的链表满足单调不减规则。


# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code he
        pHead = pHead1
        temp1 = pHead1
        temp2 = pHead2
        while temp1 and temp2:
        	if temp1.val <= temp2.val:
        		pHead.val = temp1.val
        		temp1 = temp1.next
        	else : 
        		pHead.val = temp2.val
        		temp2 = temp2.next
        	pHead = pHead.next
        if not temp1:
        	pHead.next = temp1
        if not temp2:
        	pHead.next = temp2
        return pHead