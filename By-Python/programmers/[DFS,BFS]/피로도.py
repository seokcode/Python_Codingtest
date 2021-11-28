def solution(k, dungeons):
    global answer
    answer = -1
    visited = [False] * len(dungeons)
    dfs(k, 0, visited, dungeons)
    return answer

def dfs(k, cnt, visited, dungeons):
        global answer
        answer = max(answer, cnt)

        for i in range(len(dungeons)):
            if not visited[i] and dungeons[i][0] <= k:
                visited[i] = True
                dfs(k-dungeons[i][1], cnt+1, visited, dungeons)
                visited[i] = False