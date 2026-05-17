from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_anagrams = defaultdict(list)
        for word in strs:
            key = tuple(sorted(list(word)))
            group_anagrams[key].append(word)

        return list(group_anagrams.values())
