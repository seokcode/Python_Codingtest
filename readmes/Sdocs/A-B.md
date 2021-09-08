# A->B
> **삼성 SW 역량 테스트 기출**
>
> **Silver 1**
>
> **2021-02-11**
>
> [B16953](https://www.acmicpc.net/problem/16953)


## Sol

BFS 혹은 그리디로도 풀 수 있는 문제였다(Swift는 둘 다 12ms).


<br>

문제에서 크게 고려해야 할 것은 3가지 경우이다.

**1. 2를 곱하기**  
**2. 최우측에 1을 추가하는 경우**  
**3.위 두가지 방법으로 b를 만들 수 없다면 -1을 출력한다**


<br>
 

 
 
## BFS 풀이
```swift
import Foundation

let number = readLine()!.split(separator: " ").map{Int($0)!}
var start = number.first!
let goal = number.last!
var result = Int.max

func bfs(_ value: Int, _ count: Int) {
    if value == goal {
        result = min(result, count)
    } else if value > goal {
        return
    }
    
    bfs(value*2, count+1)
    bfs(value*10 + 1, count+1)
}

bfs(start, 0)
result == Int.max ? print(-1) : print(result+1)
```

## 그리디 풀이
```swift
import Foundation

let number = readLine()!.split(separator: " ").map{Int($0)!}
var A = number.first!
var B = number.last!
var count = 1 // 답에 + 1 해줘야해서 여기서 미리 해주는거

// 그리디연산 시작 B -> A로
while true {
    if B == A {
        break
    // 더 이상의 연산이 불가능하거나 B가 A보다 작아졌다면 같아지는것이 불가능함
    } else if (B%2 != 0 && B%10 != 1) || (B < A) {
        count = -1
        break
    // 2로 나눠질 수 있다면 제일 베스트니까 먼저 시행
    } else if B % 2 == 0 {
        B /= 2
        count += 1
    // 오른쪽에 1을 더한 숫자라면 5 -> 51이 되는거니까 10으로 나누었을 때 나머지가 1
    } else if B % 10 == 1 {
        B /= 10
        count += 1
    }
}

print(count)
```