class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_to_count = collections.Counter(s)
        for i, c in enumerate(s):
            if char_to_count[c] == 1:
                return i

        return -1
