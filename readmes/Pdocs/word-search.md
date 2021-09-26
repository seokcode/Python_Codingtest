# Word Search
> **Medium**
>
> **2021-09-26**
>
> **[Leetcode: Word Search](https://leetcode.com/problems/word-search)**


## Sol

단어의 시작 문자와 일치하는 곳을 찾고 그 위치부터 dfs를 통해 탐색해나갔다.  

> any를 새로알게되었당
### any(iterableValue)
전달받은 자료형의 element 중 하나라도 True일 경우 True를 돌려준다. (만약 empty 값을 argument로 넘겨주었다면 False를 돌려준다.)

* iterable 자료형내 element가 모두 False일 경우
    ```python
    >>> a = [False,False,False]
    >>> any(a)
    False
    ```
* iterable 자료형내 element 중 True가 있을 경우
    ```python
    >>> a = [True,False,True]
    >>> any(a)
    True
    ```

## 답안
> Runtime: 5620 ms, faster than 79.23% of Python3 online submissions for Word Search.
> Memory Usage: 14.4 MB, less than 41.51% of Python3 online submissions for Word Search.
```python
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW, COL = len(board), len(board[0])
        goal = list(word)
        visit = [[False] * len(board[0]) for _ in range(len(board))]
        
        for row in range(ROW):
            for col in range(COL):
                if board[row][col] == goal[0]:
                    visit[row][col] = True # visit
                    if self.findWord(visit, board, row, col, 1, goal):
                        return True
                    visit[row][col] = False # recover
                    
        return False
    
    def findWord(self, visit, board, row, col, idx, goal):
        ROW, COL = len(board), len(board[0])
        dx = [0,-1,0,1]
        dy = [1,0,-1,0]
        
        # found word
        if idx == len(goal):
            return True
        
        for d in range(4):
            nx = row+dx[d]
            ny = col+dy[d]
            # next location exists in range
            if 0 <= nx < ROW and 0 <= ny < COL:
                # next location is valid character && visit not yet
                if board[nx][ny] == goal[idx] and not visit[nx][ny]:
                    visit[nx][ny] = True # visit
                    if self.findWord(visit, board, nx, ny, idx+1, goal): 
                        return True
                    visit[nx][ny] = False # recover
                
        return False 
```