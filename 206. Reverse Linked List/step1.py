# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []
        node = head
        while node is not None:
            nodes.append(node)
            node = node.next

        if not nodes:
            return head

        head = nodes.pop()
        node = head
        i = len(nodes)
        while i > 0:
            top = nodes.pop()
            top.next = None
            node.next = top
            node = node.next
            i -= 1

        return head
