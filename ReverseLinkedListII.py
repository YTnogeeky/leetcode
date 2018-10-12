class Solution(object):
    def reverseBetween(self, head, m, n):
        if m == n:
            return head

        dummy = ListNode(0)
        dummy.next = head
        p = dummy

        for i in range(m - 1):
            p= p.next
        
        # reverse the [m, n] nodes
        reverse = None
        cur = p.next
        for i in range(n - m + 1):
            next = cur.next
            cur.next = reverse
            reverse = cur
            cur = next

        p.next.next = cur
        p.next = reverse

        return dummy.next
