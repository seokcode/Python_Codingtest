# Longest Substring Without Repeating Characters
> **Medium**
>
> **2021-07-31**
>
> **[Leetcode: Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters)**


## Sol
### `먼저 내가 푼 방법은 이렇다.`
1. for문은 s의 길이만큼 한번만 돈다. 
2. for문을 돌며 subArr에 연속되는 부분 문자열을 이어나간다.
    * 만약 subArr에 이미 있는 숫자라면 이어나가는것을 멈추고 그 문자열을 compareArr에 저장해둔다.
    * 그리고 현재 문자와 subArr의 마지막 문자열이 같은지 찾는다.
        * 만약 같지 않다면 subArr에서 현재 문자의 위치를 찾고 그 이후부터 subArr를 다시 이어나간다.
        * 같다면 중복되는 위치가 이미 바로 앞이기 때문에 그 전까지의 문자열은 쓸 수 없으므로 subArr를 초기화해준다.

3. for문이 1회 돌고나면 subArr와 compareArr에 들어있는 문자열 중 최대 길이를 return해준다.

이 경우의 시간 복잡도는 최대 O(n^2)이다. `idx = subString.find(c)` 얘 땜시


### `이렇게 풀지 않고 더 좋은 방법은 해시맵과 head와 tail을 이용하는 방법이다. `

1. 마찬가지로 for문은 s의 길이만큼 한번만 돈다.
2. tail을 한칸씩 옮겨가며 문자를 방문한다
3. 한번 방문한 문자는 자신을 key로 한 채, 해시맵에 현재 자신의 인덱스 위치를 value로 가지고 등록된다.
4. 만약 두번째 방문하는 문자가 생긴다면 해시맵에서 value를 현재 위치로 업데이트 시켜준다. 그리고 head를 해당 문자를 처음 방문한 위치의 다음칸으로 한칸 밀어준다(원래 내가 푼 방법에서 2번 subArr를 이어나가는 부분)

이해가 안된다면 [이 곳](https://leetcode.com/problems/longest-substring-without-repeating-characters/solution/)에 동영상과 함께 설명이 되어 있다.


## 내 답안
> Runtime: 114 ms, faster than 26.35% of Python3 online submissions for this problems  
> Memory Usage: 14.4 MB, less than 54.50% of Python3 online submissions for this problems
```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subArr, compareArr = [], []
        for c in s:
            if not subArr or (c not in subArr):
                subArr.append(c)
            else:
                if not compareArr:
                    compareArr = subArr
                else:
                    if len(subArr) > len(compareArr):
                        compareArr = subArr
                
                if subArr[-1] != c:
                    subString = "".join(subArr)
                    idx = subString.find(c)
                    subArr = list(subString[idx+1:])
                else:
                    subArr = []
                subArr.append(c)
        
        return max(len(subArr), len(compareArr))
```


## 더 좋은 답안 
> Runtime: 65 ms, faster than 57.64% of Python3 online submissions for this problems  
> Memory Usage: 14.4 MB, less than 54.50% of Python3 online submissions for this problems
```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        # mp stores the current index of a character
        mp = {}

        i = 0
        # try to extend the range [i, j]
        for j in range(n):
            if s[j] in mp:
                i = max(mp[s[j]], i)

            ans = max(ans, j - i + 1)
            mp[s[j]] = j + 1

        return ans
```