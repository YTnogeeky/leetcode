# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        res, stack = [], []
 
        while True:
            while root:
                stack.append(root)
                res.append(root.val)
                root = root.left
            if not stack:
                return res
            node = stack.pop()
            root = node.right
        return res
