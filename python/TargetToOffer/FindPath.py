# 题目描述
# 输入一颗二叉树和一个整数，
# 打印出二叉树中结点值的和为输入整数的所有路径。
# 路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。 	

# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if not root:
        	return []
        paths = self.AllPath(root)
        res = []
        for path in paths:
        	if sum(path) == expectNumber:
        		res.append(path)
       	return res

    def AllPath(self, root):
    	if not root:
    		return []
    	if not root.left and not root.right:
    		return [[root.val]]
    	res = []
    	leftside = self.AllPath(root.left)
    	rightside = self.AllPath(root.right)
    	for i in leftside+rightside:
    		res.append([root.val]+i)
    	return res

if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(4)
    root.left.left = TreeNode(4)
    root.left.left.left = TreeNode(5)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    print(s.FindPath(root, 12))

