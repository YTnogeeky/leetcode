class Codec:
    def serialize(self, root):
        res, stk = [], []
        while stk or root:
            if root:
                res.append(str(root.val))
                stk.append(root)
                root = root.left
            else:
                root = stk.pop()
                root = root.right
        return ' '.join(res)

    def deserialize(self, data):
        if not data:
            return None
        data = map(int, data.split(' '))
        stk = []
        root = node = TreeNode(data[0])
        for n in data[1:]:
            if n < node.val:
                node.left = TreeNode(n)
                stk.append(node)
                node = node.left
            else:
                while stk and stk[-1].val < n:
                    node = stk.pop()
                node.right = TreeNode(n)
                node = node.right
        return root
