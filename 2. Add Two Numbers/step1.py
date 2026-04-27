# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        node = head
        carry = 0

        while l1 is not None or l2 is not None:
            if l1 is not None and l2 is not None:
                n = (l1.val + l2.val + carry) % 10
                carry = (l1.val + l2.val + carry) // 10
                l1 = l1.next
                l2 = l2.next
            elif l1 is not None:
                n = (l1.val + carry) % 10
                carry = (l1.val + carry) // 10
                l1 = l1.next
            elif l2 is not None:
                n = (l2.val + carry) % 10
                carry = (l2.val + carry) // 10
                l2 = l2.next

            node.val = n
            if l1 is not None or l2 is not None:
                node.next = ListNode(0)
                node = node.next

        if carry == 1:
            node.next = ListNode(1)
            node = node.next

        return head
