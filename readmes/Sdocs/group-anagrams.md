# Group Anagrams
> **Medium**
>
> **2021-03-03**
>
> **[Leetcode: Group-Anagrams](https://leetcode.com/problems/group-anagrams)**


## Sol
dictionary를 이용하여 같은 단어끼리 모은 뒤 각 key값들의 value들을 return해주어 해결하였다.


## 답안
```swift
class Solution {
    func groupAnagrams(_ strs: [String]) -> [[String]] {
        var dict: [String: [String]] = [:]
        var answer: [[String]] = []
        for anagram in strs{
            var temp = Array(anagram)
            temp = temp.sorted()
            var list = temp.map { String($0) }.joined(separator:"")
            if let exist = dict[list] {
              dict[list] = exist + [anagram]
            }
            else {
              dict[list] = [anagram]
            }
       }
        
        dict.forEach {
            answer.append($0.value)
        }
        return answer
    }
}
```

## Better Code
```swift
class Solution {
    func groupAnagrams(_ strs: [String]) -> [[String]] {
         if strs.count == 0 { return [[""]] }
         var dict = [String:[String]]()
        
        var res = [[String]]()
        for str in strs {
            dict[String(str.sorted()), default:[]].append(str)
        }
        
        for anagrams in dict.values {
            res.append(anagrams)
        }
        
        return res
    }
}
```
