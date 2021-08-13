# Group Anagrams

from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = []
        d = defaultdict(list)
        for i in strs:
            temp = sorted(i)
            d["".join(temp)].append(i)

        for i in d:
            answer.append(d[i])

        return answer