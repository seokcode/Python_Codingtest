# Unique Paths
> **Medium**
>
> **2021-11-09**
>
> **[Leetcode: Unique Paths](https://leetcode.com/problems/unique-paths)**


## Sol
처음엔 BFS로 접근했지만 아무래도 모든 시작점에서 갈 수 있는 모든 경로를 조사해야하다보니 시간초과가 났다.

DP로 접근하려면 먼저 규칙을 찾아야한다. 로봇은 오른쪽과 아래 방향으로만 움직일 수 있다. 이 말은 다르게 보면 각 칸은 자신의 왼쪽과 위로부터 올 수 있다는 점이다.

따라서 각 칸 `dp[i][j]`으로 올 수 있는 방법의 수는 자신의 위(`dp[i - 1][j]`) + 자신의 왼쪽(`dp[i][j - 1]`) 방법의 수의 합과 같다.   
또한, 시작점 (0,0)을 기준으로 (0,0)~(0,N)까지와 (0,0)~(M,0)까지는 무조건 도달할 수 있는 곳이다.

|0|0|0|
|:--:|:--:|:--:|
|0|0|0|

⬇️

|1가지|1가지|1가지|
|:--:|:--:|:--:|
|1가지|2가지|`3가지`|


## 답안
> Runtime: 0 ms, faster than 100.00% of Swift online submissions for Unique Paths.
> Memory Usage: 13.9 MB, less than 30.14% of Swift online submissions for Unique Paths.
```swift
class Solution {
    func uniquePaths(_ m: Int, _ n: Int) -> Int {
        var dp = Array(repeating: Array(repeating: 0, count: n), count: m)
        
        (0..<m).forEach {
            dp[$0][0] = 1
        }
        
        (0..<n).forEach {
            dp[0][$0] = 1
        }
        
        (1..<m).forEach { i in
            (1..<n).forEach { j in
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
            }
        }
        
        return dp[m-1][n-1]
    }
}
```