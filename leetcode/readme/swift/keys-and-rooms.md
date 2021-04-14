# Keys and Rooms  
> **Medium**
>
> **2021-04-14**
>
> **[Leetcode: Keys and Rooms](https://leetcode.com/problems/keys-and-rooms)**


## Sol
```xml
Input(rooms): [[1,3],[3,0,1],[2],[0]]
Output: false
Explanation: We can't enter the room with number 2.
```
위와 같은 Input이 주어지면 rooms는 0,1,2,3번의 총 4개의 방을 가지고 있으며, 0번 방에는 1,3번 방으로 가는 열쇠가, 1번 방에는 3,0,1번 방으로 가는 열쇠.. 이런식의 문제이다. 모든 방을 다 방문할 수 있는 경우에만 true를 return한다(처음엔 0번 방에서 시작한다.)


나는 컬렉션 타입인 Set과 재귀함수를 활용하여 문제를 해결하려했다. 근데 Set에는 contain함수가 없는 줄 알고 Array로 변경하여 제출했는데 그 코드가 아래의 답안1 코드이다.
통과는 했으나, 주석에 달아놨듯 상당히 꾸역꾸역 느리게 통과했다. 시간 복잡도는 O(n)* O((각 방에 있는 키의 갯수)) 정도 될 것 같다. 왜냐 Array의 contains 메서드는 시간복잡도가 O(n)이기 때문이다.


### 답안1
```swift
// Runtime: 236 ms, faster than 5.56% of Swift online submissions for Keys and Rooms.
// Memory Usage: 14.5 MB, less than 24.31% of Swift online submissions for Keys and Rooms.
class Solution {
    func canVisitAllRooms(_ rooms: [[Int]]) -> Bool {
        var v: Array<Int> = [0]
            
        func visit(_ keys: [Int]) {
            for i in keys{
                if !v.contains(i) {
                    v.append(i)
                    visit(rooms[i])   
                }                
            }
        }
        
        visit(rooms[0])
        
        if v.count != rooms.count {
            return false
        }else{
            return true
        }
    }
}
```

그래서 다시 제출한 코드가 답안2의 코드. Set의 contains는 시간복잡도가 O(1)이다. 그것만 바꿔서 제출했더니 보는것처럼 런타임이 확 줄었다. O(1)*O(각 방에 있는 키의 갯수) 정도 일 것이다.

### 답안2
```swift
// Runtime: 36 ms, faster than 98.61% of Swift online submissions for Keys and Rooms.
// Memory Usage: 14.9 MB, less than 8.33% of Swift online submissions for Keys and Rooms.
class Solution {
    func canVisitAllRooms(_ rooms: [[Int]]) -> Bool {
        var v: Set<Int> = [0]
            
        func visit(_ keys: [Int]) {
            for i in keys{
                if !v.contains(i) {
                    v.insert(i)
                    visit(rooms[i])   
                }                
            }
        }
        
        visit(rooms[0])
        
        if v.count != rooms.count {
            return false
        }else{
            return true
        }
    }
}
```


### 답안3
사실 이 방법이 가장 빠르다ㅎㅎ Set 안쓰고 contains도 안 쓴 코드 근데 나는 이것보다 답안2의 코드가 더 빨리 생각나서 그걸로 풀었다.

```swift
// Runtime: 32 ms, faster than 100.00% of Swift online submissions for Keys and Rooms.
// Memory Usage: 14.1 MB, less than 83.33% of Swift online submissions for Keys and Rooms.
class Solution {
    func canVisitAllRooms(_ rooms: [[Int]]) -> Bool {
        var keys: [Int] = Array(repeating: -1, count: rooms.count)
        keys[0] = 0
        var visited = [0]
        var num = 0
        
        while num < visited.count {
            for i in rooms[visited[num]]{
                if keys[i] == -1 {
                    keys[i] = 0
                    visited.append(i)
                }
            }
            if visited.count == rooms.count{
                return true
            }else{
                num += 1   
            }
        }
        
        return false
    }
}
```