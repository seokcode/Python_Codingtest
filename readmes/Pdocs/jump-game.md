# Jump Game
> **Medium**
>
> **2021-10-02**
>
> **[Leetcode: 55. Jump Game](https://leetcode.com/problems/jump-game/)**


## Sol 

Jump Game II 문제처럼 Goal에 도달하는 최소 횟수가 아니라 Goal에 도달할 수 있는지 여부만을 확인하면 되는 문제이다. DFS로 풀라그랬더니 메모리 초과가 나서 투포인터로 다시 풀어따..

## 틀린 답안
> 메모리 초과
```python
from collections import deque

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cnt, cur, destination = 0, 0, len(nums)-1
        Q = deque([(0,0)])
        
        while Q:
            cur, cnt = Q.popleft()
            if cur >= destination:
                return True
            
            for m in range(1, nums[cur]+1):
                Q.append((cur+m, cnt+1))
        
        return False
```


[2,3,1,1,4] 로 예를 들자.

1. [`2`,3,1,1,4]  
    * lp: 0, rp: 0, furthest: max(0+2) = 2
2. [2,`3,1`,1,4]
    * lp, rp = rp+1, furthest
    * lp: 1, rp: 2, furthest: max(1+3, 1+2) = `4` -> 목적지 도달, 끝!

[3,2,1,0,4] 로 예를 들자.

1. [`3`,2,1,0,4]
    * lp: 0, rp: 0, furthest: max(0+3) = 3
2. [3,`2,1,0`,4]
    * lp, rp = rp+1, furthest
    * lp: 1, rp: 3, furthest: max(1+2, 2+1, 3+0) = 3
2. [3,2,1,0,4]
    * lp, rp = rp+1, furthest
    * lp: 4, rp: 3 -> 전진 불가, 끝!

## 답안
```python
class Solution:        
    def canJump(self, nums: List[int]) -> bool:
        lp, rp, furthest = 0, 0, 0
        destination = len(nums)-1
        
        # 오른포인터가 목적지 이상으로 넘어가면 종료
        while rp < destination:
            # 왼포인터가 더 커지면 목적지 도달 불가능을 의미
            if lp > rp:
                return False
            
            # 1. lp, rp+1 == 현재 위치 ~ 현재 위치에서 가장 멀리 갈 수 있는 위치
            # 2. i+nums[i] == 각 위치 별로 다음에 점프 뛰어 갈 수 있는 곳
            furthest = max([i+nums[i] for i in range(lp, rp+1)])

            # 제일 멀리 뛸 수 있는 위치가 furthest에 들어있다.
            # lp에는 이전에 가장 멀리 뛸 수 있는 위치였던 rp+1로 초기화해준다.
            # 근데 여기서 lp가 rp보다 커지면 더 이상 전진 할 수 없다는 뜻이므로 다음 if문에서 False Return
            lp, rp = rp+1, furthest
            
        return True    
```