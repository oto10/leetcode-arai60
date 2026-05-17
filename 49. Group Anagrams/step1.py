from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_anagrams = defaultdict(list)
        for s in strs:
            char_bags = list(s)
            key = tuple(sorted(char_bags))
            group_anagrams[key].append(s)

        return list(group_anagrams.values())
