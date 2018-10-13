# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        # write your code here
        if head == None:
            return None
            
        myMap = {}
        nHead = RandomListNode(head.label)
        myMap[head] = nHead
        p = head
        q = nHead
        while p:
            if p.next:
                q.next = RandomListNode(p.next.label)
                myMap[p.next] = q.next
            else:
                q.next = None
                
            p = p.next
            q = q.next
        
        t = head
        while t:
            if t.random:
                myMap[t].random = myMap[t.random]
            t = t.next
        return nHead
