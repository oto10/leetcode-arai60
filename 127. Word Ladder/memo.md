## Step1

まず、beginWord と wordList 内の各単語を比較し、beginWord と「beginWord の文字数 - 1 文字」が一致する単語を wordList の中から探す方針を思いついた。　　
一致する単語が見つかった場合は、変換シーケンスに含まれる単語数を表す num_words をインクリメントし、その単語を次の比較対象にする。　　
また、一度見つけた単語は再び探索しないように、wordList から削除していけばよいと考えた。　　
しかし、この考え方ではエッジケースを見落としているのではないかという懸念があり、具体的な実装方法も分からなかったため、解答を参考に実装した（コードは `step1.py` 参照）。　　

### 所感

- 私の最初の方針（見つかった1つの単語から次へ進む）では、最短経路を保証できない
    - 到達できるすべての候補を調べる必要がある
- ノードを単語、エッジを1文字だけ異なる関係とした、重みなしグラフの最短経路問題として考える

### 計算量

N = len(wordList) // 単語数　　
L = len(beginWord) // 1単語の文字数　　
とおくと、　　
　　
**時間計算量**
- O(NL^2)
    - 一度見つけた単語は削除していくため、最大でも N 個の単語を探索する
    - next_word は L × 26 個作る
    - next_word を作るのに、O(L) かかる

**空間計算量**
- O(N)
    - 入力 wordList とは別に追加でメモリを使っているのは、words = set(wordList)
    - words は最大 N 個

**実行時間（概算）**
- 0.5 秒
    - 制約の最大値 N = 5000, L = 10 を O(NL^2) に代入し、10^6 step/s で除算して求めた

## Step2

- 変数名 `trans_seq` を `words_with_num_words` に変更した
    - deque に入っているのは、変換シーケンスそのものではなく、これから探索する単語とシーケンスに含まれる単語数のため
- 以下の処理を関数化した `generate_next_word_candidates()`

```python
for i in range(len(word)):
    for char in "abcdefghijklmnopqrstuvwxyz":
        next_word = word[:i] + char + word[i + 1:]
```

- "abcdefghijklmnopqrstuvwxyz" を `string.ascii_lowercase` に変更した

## Step3

10分以内に3回連続でエラーを出さずに書いてアクセプトされた。