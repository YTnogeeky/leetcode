class Solution(object):
    def deleteDuplicates(self, head):
        p = head
        while p:
            while p.next and p.next.val == p.val:
                p.next = p.next.next     # skip duplicated node
            p = p.next     # not duplicate of current node, move to next node
        return head
