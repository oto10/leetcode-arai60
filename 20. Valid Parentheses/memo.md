# Step1
入力として例えば、 `s = "([])"` が与えられたと仮定する。
文字列 s を先頭 1 文字目から走査していき、 N 文字目で最初の閉じ括弧が表れた場合、その閉じ括弧の種類が N - 1 文字目の開き括弧と対応付くかをチェックしていけば良さそうである。
Stack は LIFO であるから、 s の先頭要素から開き括弧をひたすら push していき、閉じ括弧が来た時点で、 その 1 つ前の開き括弧と対応付くかを判定する。対応付いた場合は pop する。文字列 s を全走査した後で stack が空になっていれば、入力 s は有効であり、出力として True を返す。

初めに以下のコードを書いたが、 Runtime Error となった。

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ['(', '{', '[']:
                stack.append(c)
            elif c == ')':
                if stack[-1] == '(':
                    stack.pop()
            elif c == '}':
                if stack[-1] == '{':
                    stack.pop()
            elif c == ']':
                if stack[-1] == '[':
                    stack.pop()

        if not stack:
            return True
        else:
            return False
```

原因として以下が挙げられる。
- 条件式で stack[-1] を確認する前に、 stack が空でないか確認していない。
    - `s = ")"` の場合、 IndexError になってしまう。
- 閉じ括弧が対応付いていない時点で return False していない。
    - `s = "]"` の場合、 出力が false ではなく true になってしまう。

# Step2
- ネストされた if 文の条件式を invalid なケースとした。
 - valid 判定よりも先に invalid なケースを弾いた方が、安全だと感じたため。
 - Python の or は左から評価され、左が True の時点で右側は評価されないため。

# Step3
10分以内に3回連続でエラーを出さずに書いてアクセプトされた。

# コードレビューでのフィードバックをもとに改善したコード
```python
class Solution:
    def isValid(self, s: str) -> bool:
        open_brackets = []
        open_to_close = {
            "(": ")",
            "{": "}",
            "[": "]",
        }

        for bracket in s:
            if bracket in open_to_close.keys():
                open_brackets.append(bracket)
            for opening_bracket in open_to_close.keys():
                if bracket == open_to_close[opening_bracket]:
                    if not open_brackets or open_brackets[-1] != opening_bracket:
                        return False
                    open_brackets.pop()

        return not open_brackets
```
