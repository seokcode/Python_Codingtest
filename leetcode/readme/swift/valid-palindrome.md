# Valid Palindrome
> **Easy**
>
> **2021-04-07**
>
> **[Leetcode: Valid-Palindrome](https://leetcode.com/problems/valid-palindrome)**


## Sol
펠린드롬이란 'bob'처럼 앞,뒤가 똑같은 문자열을 말한다.  
주어지는 문자열은 영문,숫자로만 이루어져있기 때문에 소문자로 변환한 뒤, 정규식검사를 통해 영문,숫자들만 찾고 join함수와 lower함수를 통해 합쳐주었다.  
길이가 1인 경우에는 모두 다 펠린드롬이 성립하므로 true를 반환 해주고, 길이가 n인 경우에는 (s[0],s[n-1]), (s[1],s[n-1-1])...와 같이 같아야하므로  
하나라도 다르다면 false를 return해주었다.


## 답안
```swift
class Solution {
    func isPalindrome(_ s: String) -> Bool {
        if s.count == 1{
            return true
        }
        
        let re: String = "[a-z0-9+]"
        let new_s = Array(s.lowercased().checkRegex(regex: re).joined(separator: ""))
        let range = new_s.count/2
        
        for i in 0..<range{
            if new_s[i] != new_s[new_s.count-1-i]{
                return false
            }    
        }
        return true
    }
}

extension String{
    func checkRegex(regex: String) -> [String] {
        
        do {
            let regex = try NSRegularExpression(pattern: regex)
            let results = regex.matches(in: self,
                                        range: NSRange(self.startIndex..., in: self))
            return results.map {
                String(self[Range($0.range, in: self)!])
            }
        } catch let error {
            print("invalid regex: \(error.localizedDescription)")
            return []
        }
    }
}
```

## 더 좋은 답안
> **내 풀이랑 다른점**  
> Character형일 경우 isLetter, isNumber, isASCII 등의 메서드를 사용할 수 있는데 이 풀이는 그 특성을 이용하여 정규식 검사를 하지 않았다.  
> 또한 start,end를 통해 비교해야하는 위치를 계산해주었다. 
```swift
class Solution {
    func isPalindrome(_ s: String) -> Bool {
        if s.count == 1{
            return true
        }
        var start = 0, end = s.count - 1
        let arr = Array(s.lowercased())
        
        while start < end{
            while start < end && !arr[start].isAlphaNumeric{
                start += 1
            }
            while start < end && !arr[end].isAlphaNumeric{
                end -= 1
            }
            if arr[start] != arr[end]{
                return false
            }
            start += 1
            end -= 1
        }
        return true
    }
}

extension Character {
    var isAlphaNumeric: Bool {
        return isLetter || isNumber
    }
}
```