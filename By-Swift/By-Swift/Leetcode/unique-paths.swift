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