# 题目描述
# 输入一个链表，输出该链表中倒数第k个结点。

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if not head:
        	return head
        after = ListNode(head.val)
        for i in range(k):
        	if not after:
        		return after
        	after = after.next
        before = ListNode(head.val)
        while after:
        	after = after.next
        	before = before.next
        return before