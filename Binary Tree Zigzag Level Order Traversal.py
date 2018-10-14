# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: 
            return []
        res = [] 
        q = [root]
        flag = 1
        
        while q:
            temp=[]
            for _ in xrange(len(q)):
                node=q.pop(0)
                temp.append(node.val)
                if node.left: 
                    q.append(node.left)
                if node.right: 
                    q.append(node.right)
            res.append(temp[::flag])
            flag*=-1
        return res
