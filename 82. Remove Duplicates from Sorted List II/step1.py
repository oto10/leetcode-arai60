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
                copy = node.next

                while copy.next and copy.val == copy.next.val:
                    copy = copy.next

                node.next = copy.next

            else:
                node = node.next

        return dummy_head.next