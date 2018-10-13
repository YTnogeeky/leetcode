# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        p= dummy
        carry  = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            
            # 运算未结束新建一个节点用于储存答案，否则退出循环
            p.next = ListNode(carry % 10)
            carry /= 10
            p = p.next
           
        return dummy.nextAdd Two Numbers
