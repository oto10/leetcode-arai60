from collections import deque

def generate_next_word_candidates(word):
    for i in range(len(word)):
        for c in string.ascii_lowercase:
            yield word[:i] + c + word[i + 1:]

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        words = set(wordList)
        if endWord not in words:
            return 0

        words_with_num_words = deque([(beginWord, 1)])
        while words_with_num_words:
            word, num_words = words_with_num_words.popleft()
            for next_word in generate_next_word_candidates(word):
                if next_word == endWord:
                    return num_words + 1

                if next_word in words:
                    words.remove(next_word)
                    words_with_num_words.append((next_word, num_words + 1))

        return 0
