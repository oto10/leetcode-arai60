# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nodes_set = set()
        current_node = head

        while current_node is not None:
            if current_node in nodes_set:
                return True
            nodes_set.add(current_node)
            current_node = current_node.next

        return False