# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        nodes = []
        node = head
        while node is not None:
            nodes.append(node)
            node = node.next

        head = nodes.pop()
        node = head
        for _ in range(len(nodes)):
            top = nodes.pop()
            top.next = None
            node.next = top
            node = node.next

        return head
