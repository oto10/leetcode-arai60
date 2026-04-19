## step1
set() で重複をまとめたあとに ListNode クラスへ変換すればよいと思ったが、変換方法を考えているうちに5分ほど経ってしまったので、新井さんの解説動画を見た。
解説動画を見て、連結リストのノードを削除する際は、前後のポインタを付け替えて該当ノードをリストから外す方法を思い出した。
以下は、解説を見る前に最初に書いたコードである。

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = set()
        node = head

        while node:
            if node.val not in nodes:
                nodes.add(node.val)

            node = node.next

        return sorted(list(nodes))
```

## step2
先頭ノードが None かどうか判定する条件式を while の条件式にまとめた。

## step3
Step2のコードを10分以内に3回連続で書けるようにした。