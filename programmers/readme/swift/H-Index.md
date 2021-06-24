# H-Index
> **Lv2**
>
> **2021-06-24**
>
> [프로그래머스: 42747](https://programmers.co.kr/learn/courses/30/lessons/42747)


## Sol
> 어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index입니다.
>
>제한사항
>
>과학자가 발표한 논문의 수는 1편 이상 1,000편 이하입니다.
>논문별 인용 횟수는 0회 이상 10,000회 이하입니다.

<kbd>풀이방법</kbd>

1. 브루트포스  
n(1,000) * m(10,000) = 10,000,000가지의 경우의 수로 제한 시간 내 통과가 되기 때문에 그냥 브루트포스를 이용하여도 무방하다. <kbd>시간복잡도 O(n*m)</kbd>

2. 이분탐색법  
하지만 좀 더 효율적인 방법으로 풀고싶어서 나는 이분탐색으로도 한번 더 풀어보았다.
filter는 O(n)의 시간복잡도를 띄기 때문에 이분탐색을 사용하면 총 <kbd>시간복잡도 O(nlogm)</kbd>만에 해결할 수 있다.



## 답안1-정렬,브루트포스
```swift
import Foundation

func solution(_ citations:[Int]) -> Int {
    var cit = citations.sorted()
    var h = 0
    var answer = 0
    
    while true {    
        let citated = cit.filter{$0 >= h}.count
        
        if citated >= h {
            answer = h
            h += 1
        } else {
            return answer
            break
        }
    }
}
```

## 답안2-이분탐색법
```swift
import Foundation

func solution(_ citations:[Int]) -> Int {
    var low = 0
    var high = citations.max()!
    
    while low <= high {
        let mid = (low+high)/2
        let citated = citations.filter{$0 >= mid}.count
        
        if citated < mid {
            high = mid-1
        } else {
            low = mid+1
        }
    }
    
    return high
}
```