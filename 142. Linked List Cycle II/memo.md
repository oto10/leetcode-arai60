## Step1
5分以内にset()を用いた解法で解けた。
問題文より141. Linked List Cycle の解法ロジックを元に、各戻り値を変更すれば良いのだと思った。

# Step2
while の条件式を可読性の観点から `while node is not None` から `while node` と簡潔にした。

# Step3
Step2のコードを10分以内に3回連続で書けるようにした。

# フロイドの循環検出法で解いたコード
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        fast = head
        slow = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if fast is slow:
                break
        else:
            return None

        slow = head
        while slow is not fast:
            slow = slow.next
            fast = fast.next

        return slow
```