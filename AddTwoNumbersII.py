class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        p = dummy
        c1, c2 = [], []
        num = 0
        nums = []
        while l1:
            c1.append(l1.val)
            l1 = l1.next
        while l2:
            c2.append(l2.val)
            l2 = l2.next
        while c1 or c2:
            if c1:
                num += c1.pop()
            if c2: 
                num += c2.pop()
            nums.append(num % 10)
            num /= 10
        if num!=0:
            nums.append(num)

        while nums:
            p.next = ListNode(nums.pop())
            p = p.next
        return dummy.next
