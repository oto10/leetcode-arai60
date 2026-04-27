## step1
ListNode → List 型と、バラして足し合わせた後に、再び ListNode に変換して各ノードを繋げれば解けそうだと考えた。
しかし以下のコードを記述する過程で詰まった。

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_list = []
        l2_list = []

        if l1 is None:
            return l2
        if l2 is None:
            return l1

        while l1 is not None or l2 is not None:
            if l1 is not None:
                l1_list.append(l1.val)
                l1 = l1.next
            if l2 is not None:
                l2_list.append(l2.val)
                l2 = l2.next

        l2_rlist = l2_list[::-1]
        l1_ans = 0
        l2_ans = 0
        n = 10 ** (len(l1_list) - 1)
        for i, j in zip(l1_list, l2_rlist):
            tmp1 = n * i
            l1_ans += tmp1
            tmp2 = n * j
            l2_ans += tmp2
            n //= 10

        l_ans = l1_ans + l2_ans
        ans_list = [int(c) for c in str(l_ans)]
        ans_node = ListNode(0)
        i = 0
        j = len(ans_list)
        head = ans_node
        while j > 0:
            tmp_node = ListNode(ans_list[i])
            ans_node.next = tmp_node
            i += 1
            j -= 1
            ans_node = ans_node.next

        return head
```
- 引数として与えられたデータ構造を無視せず（避けようとせず）、与えられたデータ構造のまま処理できるかが肝要な気がする。
- step1.py は新井さんの解説動画を参考に書いた。

## step2
- 場合分けの際に似たような処理が重複するため、処理を1本にまとめた。
- 存在しない l1 と l2 の桁を 0 として扱い、 while の条件式に carry != 0 を加えることで、条件式 carry == 1 の if 文が不要となる。

## step3
10分以内に3回連続でエラーを出さずに書いてアクセプトされた。