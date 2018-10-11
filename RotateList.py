class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None

        if head.next == None:
            return head
        dummy = ListNode(0)
        dummy.next = head
        
        p = head
        length = 1
        while p.next:
            p = p.next
            length += 1

        k = k%length

        if k == 0:
            return head

        fast = head
        slow = head

        for a in range (k):
            fast = fast.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        tmp = slow.next
        slow.next = None
        fast.next = dummy.next
        dummy.next = tmp

        return dummy.next
