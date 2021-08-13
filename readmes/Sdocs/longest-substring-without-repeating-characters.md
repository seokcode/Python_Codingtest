# Longest Substring Without Repeating Characters
> **Medium**
>
> **2021-07-31**
>
> **[Leetcode: Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters)**


## Sol

`해시맵과 head와 tail을 이용하는 방법이다. `

1. for문은 s의 길이만큼 한번만 돈다.
2. tail을 한칸씩 옮겨가며 문자를 방문한다
3. 한번 방문한 문자는 자신을 key로 한 채, 해시맵에 현재 자신의 인덱스 위치를 value로 가지고 등록된다.
4. 만약 두번째 방문하는 문자가 생긴다면 해시맵에서 value를 현재 위치로 업데이트 시켜준다. 그리고 head를 해당 문자를 처음 방문한 위치의 다음칸으로 한칸 밀어준다(원래 내가 푼 방법에서 2번 subArr를 이어나가는 부분)

이해가 안된다면 [이 곳](https://leetcode.com/problems/longest-substring-without-repeating-characters/solution/)에 동영상과 함께 설명이 되어 있으니 참고하자.


## 내 답안
> Runtime: 44 ms, faster than 65.92% of Swift online submissions for Longest Substring Without Repeating Characters.  
>
> Memory Usage: 14.6 MB, less than 74.31% of Swift online submissions for Longest Substring Without Repeating Characters.
```swift
class Solution {
    func lengthOfLongestSubstring(_ s: String) -> Int {
        let s = Array(s)
        var ans = 0
        var start = 0
        var update = [Character: Int]()
        
        for idx in 0..<s.count {
            if update.keys.contains(s[idx]) {
                start = max(update[s[idx]]!, start)
            }
            ans = max(ans, idx-start+1)
            update[s[idx]] = idx+1
        }
        
        return ans
    }
}
```


## 또 다른 답안 
> Runtime: 64 ms, faster than 38.75% of Swift online submissions for Longest Substring Without Repeating Characters.
>
> Memory Usage: 14.4 MB, less than 92.04% of Swift online submissions for Longest Substring Without Repeating Characters.
```swift
import Foundation

class Solution {
    func lengthOfLongestSubstring(_ s: String) -> Int {
        var length = 0, chars = [Character]()
        s.forEach({
            if chars.contains($0) {
                chars.removeSubrange(0...chars.firstIndex(of: $0)!)
            }
            chars.append($0)
            length = max(length, chars.count)
        })
        return length
    }
}
```