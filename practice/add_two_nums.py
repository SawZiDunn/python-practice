class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode()
        carry = 0
        for i in range(max(len(l1), len(l2))):
            x = l1.val + l2.val
            head.val = carry + (x % 10)
            carry = x // 10
            





        