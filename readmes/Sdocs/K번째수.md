# K번째수
> **Lv1**
>
> **2021-04-19**
>
> **[프로그래머스: 42748](https://programmers.co.kr/learn/courses/30/lessons/42748)**

## Sol
```xml
배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수를 구하려 합니다.

예를 들어 array가 [1, 5, 2, 6, 3, 7, 4], i = 2, j = 5, k = 3이라면
array의 2번째부터 5번째까지 자르면 [5, 2, 6, 3]입니다.
1에서 나온 배열을 정렬하면 [2, 3, 5, 6]입니다.
2에서 나온 배열의 3번째 숫자는 5입니다.
```
map 함수를 이용해서 배열을 자르고 정렬한 뒤 k번째 수를 구해주었다.

## 답안
```swift
import Foundation

func solution(_ array:[Int], _ commands:[[Int]]) -> [Int] {
    return commands.map({(key)in 
            return array[(key[0]-1)...(key[1]-1)].sorted()[key[2]-1]                  
    })
    
}
```