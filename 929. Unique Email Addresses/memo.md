# Step1
最初は各 email を左から1文字ずつ走査し、以下のように処理する方針を考えた。
- @ の index を sign = email.find("@") で取得し、 local name と domain name の境界として保持する。
- Python の文字列は immutable なので、文字列をリストに変換して編集できるようにする。
- local name に . があれば、del email[i] で削除する。
- local name に + があれば、 + から @ の直前までを削除する。
    - email = email[:i] + email[sign:]
- 正規化後の email を set に追加し、重複を除去する。

しかし、上記方針では実装が複雑になり手が止まってしまった。
そのため、元の email を直接編集するのではなく、事前に local と domain に分割し、 local だけを処理する方針に切り替えたところ Accept された。

**計算量**
N = len(emails), M は email 1件あたりの最大長, L は Unique な Email の個数とすると、
- 時間計算量：O (N * M^2),
    - M^2 なのは、 local に . と + が一つも出現しない場合、 email_address += c は M 回繰り返すから。
- 空間計算量：O (L * M)

# Step2
- unique_email_addresses の変数名を unique_emails に変更して簡潔にした。
- email_address += c で毎回新しい文字列を作るのではなく、文字列メソッドを使って、+ 以降を切り捨てた後に . を削除する実装に変更した。

# Step3
- 10分以内に3回連続でエラーを出さずに書いてアクセプトされた。