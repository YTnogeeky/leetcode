from heapq import*
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        
        if not lists:
            return None
        
        dummy = ListNode(0)
        p = dummy
        heap = []
        
        for node in lists:
            if node:
                heappush(heap, (node.val, node))
                
        while heap:
            tmp = heappop(heap)[1]
            p.next = tmp
            if tmp.next:
                heappush(heap,(tmp.next.val, tmp.next))
            p = p.next
            
        return dummy.next
