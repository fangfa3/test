# 题目描述
# 从上往下打印出二叉树的每个节点，同层节点从左至右打印。

# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        Node = []
        result = []
        Node.append(root)
        while Node:
        	now_node = Node.pop(0)
        	if now_node.left:
        		Node.append(now_node.left)
        	if now_node.right:
        		Node.append(now_node.right)
        	result.append(now_node.val)
        return result


if __name__ == '__main__':
	pRootA= TreeNode(3)
	pRootB = TreeNode(2)
	pRootA.left = TreeNode(2)
	pRootA.right = TreeNode(3)
	pRootA.left.left = TreeNode(4)
	pRootA.left.right = TreeNode(5) 
	pRootA.right.left = TreeNode(6)
	pRootA.right.right = TreeNode(7)
	pRootA.left.left.left = TreeNode(8)
	pRootB.left = TreeNode(10)
	pRootB.right = TreeNode(5)
	pRootB.left.left = TreeNode(8)
	S = Solution()
	print(S.PrintFromTopToBottom(pRootB))

