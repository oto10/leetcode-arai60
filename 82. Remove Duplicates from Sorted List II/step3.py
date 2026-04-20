# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0)
        dummy_head.next = head
        node = dummy_head

        while node.next and node.next.next:
            if node.next.val == node.next.next.val:
                duplicate_node = node.next

                while duplicate_node.next and duplicate_node.val == duplicate_node.next.val:
                    duplicate_node = duplicate_node.next

                node.next = duplicate_node.next

            else:
                node = node.next

        return dummy_head.next