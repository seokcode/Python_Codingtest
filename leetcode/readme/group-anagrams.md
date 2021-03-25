# Group Anagrams
> **Medium**
>
> **2021-03-03**
>
> **[Leetcode: Group-Anagrams](https://leetcode.com/problems/group-anagrams)**


## Sol
dictionary를 이용하여 같은 단어끼리 모은 뒤 각 key값들의 value들을 return해주어 해결하였다.

## 답안
```python
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
```