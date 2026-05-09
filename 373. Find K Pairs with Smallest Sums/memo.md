# Step1
- 最初に以下のコードを書いたが、 pair が重複するケースの処理をコードに落とし込めなかった。
```python
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        pairs = dict()
        for u in nums1:
            for v in nums2:
                pairs[(u, v)] = u + v

        return sorted(pairs, key=pairs.get)[:k]
```
- 解答を読んでロジックを理解した上で、アクセプトされるまで写経した（step1.py）。
- nums1.length, nums2.length <= 10^5 より、すべてのペア数は最大で 10^10 個になるので、ソートだと間に合わない。このように桁数を見積もる感覚が身についていないため、最初に全ペアをソートするやり方で解こうとしたのだと思う。
- 一般に 10^5 の場合、O(n log n) は大丈夫であるが、 O(n^2) は厳しいようだ。
- step1.py の時間計算量は O(k log k) である。 Heap の push と pop の時間計算量はそれぞれ O(log n) であり、今回 while ループは最大 k 回回るため。

# Step2
- 変数名を visited から visited_indices に変更した。
    - 値ではなく index のペアを見ていることを明確にするため。
- 変数名を candidate_heap から min_candidates に変更した。
    - 変数名にデータ構造名 heap を入れてしまっていたため。変数の役割そのものを表すようにした。
- 関数名を push_heap から add_candidate に変更した。
    - push_heap は内部実装の視点では分かりやすいが、読み手の立場で考えると「具体的に何をする関数なのか」がすぐには分かりにくいと感じたため。

# Step3
- 10分以内に3回連続でエラーを出さずに書いてアクセプトされた。



