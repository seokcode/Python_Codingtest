class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        M, N = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * N for _ in range(M)]
        
        # 시작점에 장애물이 있으면 시작조차 못하므로 목적지 도달 못함
        if obstacleGrid[0][0] == 1:
            return 0
        else:
            # 시작점까지 갈 수 있는 방법의 수는 1개
            dp[0][0] = 1
        
        # 시작점(0,0)에서 (0,N)까지와 (M,0)은 장애물만 없다면 무조건 도달할 수 있는 곳 
        # (M,0)까지 가능 경로 살펴보기: 만약 현 지점과 현 지점 위에 장애물이 없고 내 위까지 도달 할 수 있었으면 현 지점에 올 수 있는 것!
        for i in range(1, M):
            dp[i][0] = int(obstacleGrid[i][0] == 0 and obstacleGrid[i-1][0] != 1 and dp[i-1][0] == 1)
        
        # (0,N)까지 가능 경로 살펴보기: 만약 현 지점과 현 지점 왼쪽에 장애물이 없고 내 왼쪽에 도달 할 수 있었으면 현 지점에 올 수 있는 것!
        for j in range(1, N):
            dp[0][j] = int(obstacleGrid[0][j] == 0 and obstacleGrid[0][j-1] != 1 and dp[0][j-1] == 1)
    
        
        for i in range(1,M):
            for j in range(1,N):
                # 현 지점에 장애물이 없으면 진행
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                    
        return dp[M-1][N-1]