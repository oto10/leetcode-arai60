from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        words = set(wordList)
        if endWord not in words:
            return 0

        trans_seq = deque([(beginWord, 1)])
        while trans_seq:
            word, num_words = trans_seq.popleft()
            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    next_word = word[:i] + c + word[i + 1:]
                    if next_word == endWord:
                        return num_words + 1

                    if next_word in words:
                        words.remove(next_word)
                        trans_seq.append((next_word, num_words + 1))

        return 0
