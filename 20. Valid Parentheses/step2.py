class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ['(', '{', '[']:
                stack.append(c)
            elif c == ')':
                if not stack or stack[-1] != '(':
                    return False
                stack.pop()
            elif c == '}':
                if not stack or stack[-1] != '{':
                    return False
                stack.pop()
            elif c == ']':
                if not stack or stack[-1] != '[':
                    return False
                stack.pop()

        if not stack:
            return True
        else:
            return False
