# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen_nodes = set()
        current_node = head

        while current_node is not None:
            if current_node in seen_nodes:
                return True

            seen_nodes.add(current_node)
            current_node = current_node.next

        return False