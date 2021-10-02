# N Queen
> **Lv3**
>
> **2021-10-02**
>
> [프로그래머스: 12952](https://programmers.co.kr/learn/courses/30/lessons/12952)


## Sol
|(0,0)|(0,1)|(0,2)|(0,3)|
|:---:|:---:|:---:|:---:|
|(1,0)|(1,1)|(1,2)|(1,3)|
|(2,0)|(2,1)|(2,2)|(2,3)|
|(3,0)|(3,1)|(3,2)|(3,3)|

이런 체스판이 있다고 할 때 Queen은 행, 열, 대각선으로 이동하여 공격할 수 있다.

내가 만약 (2,1)에 퀸을 놓았다면 아래의 `(x,y)`표시된 곳에는 퀸을 놓을 수 없다. 

|(0,0)|`(0,1)`|(0,2)|`(0,3)`|
|:---:|:---:|:---:|:---:|
|(1,0)|`(1,1)`|`(1,2)`|(1,3)|
|`(2,0)`|(2,1)|`(2,2)`|`(2,3)`|
|`(3,0)`|`(3,1)`|(3,2)|(3,3)|

모든 방향을 점검하면서 체스판을 순회해도 되지만 체스판이 굉장히 크다고 가정했을 때에는 너무 복잡한 시간복잡도를 가지게 된다.

그래서 시간을 줄일 수 있는 과정이 몇가지 있다.  

1. 내가 퀸을 놓은 열(-), 행(|)에는 더 이상 퀸을 놓을 수 없다. 무조건 퀸을 놓고 다른 열 혹은 행으로 넘어가도 무방하다
2. 내 기준 우측 위를 바라보는 대각선(↗️)은 좌표의 x+y 값이 모두 똑같다.  
3. 내 기준 좌측 위를 바라보는 대각선(↖️)은 좌표의 x-y 값이 모두 똑같다.

위 3가지의 과정을 통해 퀸을 놓아도 되는지 체크하는 과정의 시간 복잡도를 줄일 수 있다. 

## 답안
```python
def solution(n):
    check_x = [False] * n # 내가 퀸을 놓아도 되는 열인지 체크
    cross_sum = [False] * (n*2) # 우측 위 대각선 (x+y)
    cross_dis = [False] * (n*2) # 좌측 위 대각선 (x-y), x-y < 0이 될 수 있으므로 x-y+N 
    
    return nQueens(0, n, check_x, cross_sum, cross_dis)

def nQueens(Y, X, check_x, cross_sum, cross_dis):
    cnt = 0

    # 퀸을 놓은 갯수(Y)가 놓아야 하는 퀸 갯수(X)와 같다면 배치 끝난 것
    if Y == X:
        return 1
    
    for i in range(X):
        if check_x[i] or cross_sum[abs(i+Y)] or cross_dis[i-Y+X]:
            continue
        else:
            check_x[i] = True
            cross_sum[i+Y] = True
            cross_dis[i-Y+X] = True
            
            cnt += nQueens(Y+1, X, check_x, cross_sum, cross_dis)
            
            check_x[i] = False
            cross_sum[i+Y] = False
            cross_dis[i-Y+X] = False
    
    return cnt
```