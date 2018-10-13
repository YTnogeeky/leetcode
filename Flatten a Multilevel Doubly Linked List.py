class Solution(object):
    def flatten(self, head):
        if not head:
            return
        
        dummy = Node(0,None,head,None)     
        stack = []
        stack.append(head)
        p = dummy
        
        while stack:
            root = stack.pop()

            root.prev = p
            p.next = root
            
            if root.next:
                stack.append(root.next)      
            if root.child:
                stack.append(root.child)
                root.child = None
            p = root        
            
        
        dummy.next.prev = None
        return dummy.next
