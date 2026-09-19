## Step1

(i, j) をターゲットにして上下左右を探索範囲にすることまでは思いついたが、始点 (0, 0) から for 文で回す際に、どのように島を島（一つのかたまり）として捉えるかが発想できなかったため、解答を確認した。

以下が解答を参考に書いたコードである。

```python

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        number_of_islands = 0

        def dfs(i, j):
            if i < 0 or j < 0 or i >= rows or j >= cols:
                return

            if grid[i][j] == "0":
                return

            grid[i][j] = "0"
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    number_of_islands += 1
                    dfs(i, j)

        return number_of_islands

```

- "1" (land) を1つ見つけた時点で島を発見したと考えて、見つけた "1" の上下左右のマスを全て訪問済みにする

### 計算量

**時間計算量**
- O(NM)

**空間計算量**
- O(NM)
    - DFS の再帰スタック。最悪で NM 個の land を訪問するため。

**実行時間（概算）**
- 0.009 ~ 0.09 秒

## Step2

以下のコメントを参考に、コードを修正した。
- 入力値　`grid` を直接書き換えるのをやめて、訪問先を visited で管理するように変更
    - https://github.com/Hiroto-Iizuka/coding_practice/pull/17#discussion_r2716089429
- 変数名 `rows` から `num_rows` に変更し、行数のニュアンスを持たせた（number of rows の省略形）
https://github.com/subaru-hello/leetcode-arai60/pull/19#discussion_r3535497772

## Step3

10分以内に3回連続でエラーを出さずに書いてアクセプトされた。