## Step1

TLE にはなるが、まず二重ループで解く方法を思いついたので、実際に書いてみた。

```python

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            current_sum = 0
            for j in range(i, len(nums)):
                current_sum += nums[j]
                if current_sum == k:
                    count += 1

        return count

```

- 上記コードの時間計算量は O(n^2)、空間計算量は O(1) である。
- 入力サイズは最大20000なので、ループは n(n+1)/2 より約2億回まわる。
- 累積和を用いた解法を思いつけなかったため、解答を見て、原理とコードの振る舞いを理解した。（コードは `step1.py` 記載）

### 計算量

**時間計算量**
- O(n)
- n は nums の長さ

**空間計算量**
- O(n)

## Step2

Python 標準ライブラリである `collections.defaultdict` を使うことで `.get()` メソッドを省略し、可読性を向上させた。

## Step3

10分以内に3回連続でエラーを出さずに書いてアクセプトされた。