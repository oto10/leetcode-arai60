# Step1
初めに以下のコードを書き、 Time Limit Exceeded (TLE) となった。
```python
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums


    def add(self, val: int) -> int:
        self.nums.append(val)
        sorted_nums = sorted(self.nums, reverse=True)
        return sorted_nums[self.k - 1]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
```

## 疑問点とそれに対する回答 （調べた内容） および感じたことを列挙する。
- add() の中で利用している sorted() の時間計算量は O (n log n) なので間に合いそうであるが、なぜ間に合わなかったのか。
    - 時間計算量だけでなく、入力サイズや add() の呼び出し回数、 Python での実行時間も考える必要があった。
    - 問題文に記載されている制約（入力サイズ）や `At most 10^4 calls will be made to add.` を考慮せずに実装しなかったのは悪い感覚である。
    - もし入力サイズと add() の呼び出し回数が最大の 10^4 の場合、 sorted() の合計実行時間の目安は 10^4 (回) * 10^4 * log(10^4) = 10^9 とかなり大きくなると思う。
    - 入力サイズの規模感や実行時間を見積もる感覚が身についていないため、これは今後の課題であると言える。
    - ひとまず今後問題を解く際には、制約（入力サイズなど）には注意するようにする。
- sorted() の内部実装は quick sort か。
    - 調べたら Timsort と呼ばれるものらしい。Arai60 で sort の問題まで進んだタイミングで実装を確認したい。

- 解答を見て Heap での実装を行なった（step1.py）。

# Step2
- 変数名 max_k_scores を top_k_scores に変更した。

# Step3
- 10分以内に3回連続でエラーを出さずに書いてアクセプトされた。