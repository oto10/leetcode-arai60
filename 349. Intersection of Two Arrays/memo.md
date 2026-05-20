# Step1
- 2重ループの解法と HashMap を用いる解法を思いついたため、時間計算量の観点から後者を採用した。

**計算量**
- 時間計算量は O(n + m), n = len(nums1), m = len(nums2)
- 空間計算量は O(n + m), nums1_to_exists は nums2 にしかない値でもキーが増えていくため（調べた）。

# Step2
- 以下のように & 演算子を用いることで簡潔に書けることを知った。
```python
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))
```

- また、追加条件として「片方がとても小さく、もう片方が sort 済みでとても大きい」ケースを挙げられた場合は、大きい配列に set() を使って余分なメモリを消費しなくてもいいように、 sort 済みであるという性質から二分探索を使う解法も思いつけることが大切であると学んだ。
- https://github.com/katataku/leetcode/pull/12/files#r1893968021
```python
from bisect import bisect_left

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) < len(nums2):
            small, large = nums1, sorted(nums2)
        else:
            small, large = nums2, sorted(nums1)

        intersections = set()
        for num in set(small):
            i = bisect_left(large, num)
            if i < len(large) and large[i] == num:
                intersections.add(num)

        return list(intersections)
```

- bisect_left は、同じ値が見つかった場合、その値が始まる一番左の要素のインデックスを返す
- 同じ値が見つからなかった場合、昇順を維持できる挿入位置を返す

# Step3
- 10分以内に3回連続でエラーを出さずに書いてアクセプトされた。