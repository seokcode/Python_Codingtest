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


스택을 이용해서 방문할 수 있는 곳을 저장해주었고 keys 라는 [Bool] 배열을 이용해서 모든 키를 다 가졌는지 확인해주었다.

`return True if all(keys) else False`  all이라는 함수를 새롭게 알게 되었다.


## 답안1
```python
# Runtime: 64 ms, faster than 72.92% of Python3 online submissions for Keys and Rooms.
# Memory Usage: 14.9 MB, less than 31.36% of Python3 online submissions for Keys and Rooms.
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        keys = [False]*len(rooms)
        keys[0] = True
        d = [0]
        
        while d:
            desti = d.pop()
            for i in rooms[desti]:
                if not keys[i]:
                    keys[i] = True
                    d.append(i)  
            
        return True if all(keys) else False
```