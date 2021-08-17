import Foundation

func solution(_ places:[[String]]) -> [Int] {
    var result: [Int] = []
    
    for p in places {
        let place = p.map{Array($0)}
        result.append(bfs(place))
    }
    return result
}

// 고사실 하나마다 BFS 실시
func bfs(_ place: [[Character]]) -> Int {
    let dx = [1,-1,0,0]
    let dy = [0,0,1,-1]
    var people: [[Int]] = []
    
    // 응시자 위치 파악
    // 5 * 5 고정이기 때문에 시간이 크게 다르지 않을 것이라 생각하여 그냥 한번에 응시자 위치를 다 구해놓고 시작
    for x in 0..<5 {
        for y in 0..<5 {
            if place[x][y] == "P" {
                people.append([x,y])
            }
        }
    }
    
    // 고사실 내 응시자가 거리두기를 잘 지키고 있는지 점검
    for loc in people {
        var visited = Array(repeating: Array(repeating: false, count: 5), count: 5)   
        var toGo: [[Int]] = []
        visited[loc[0]][loc[1]] = true
        toGo.append([loc[0], loc[1], 0])
        
        while !toGo.isEmpty {
            let now = toGo.removeFirst()
            let x = now[0]
            let y = now[1]
            let cost = now[2]
            
            // 한명이라도 어겼다면 0 return
            // 사람 간의 거리가 2이하인 경우 -> 무조건 방역수칙 위반
            if (cost >= 1 && cost <= 2) && place[x][y] == "P" {
                return 0
            // 거리가 3 이상이라면 -> 무조건 방역수칙 준수
            } else if cost >= 3{
                break
            }
            
            for dir in 0..<4 {
                let nx = x + dx[dir]
                let ny = y + dy[dir]
                let nc = cost + 1
                
                if (nx >= 0 && nx < 5) && (ny >= 0 && ny < 5) {
                    // 'X'(책상 = 벽)라서 더 나아가지 못하거나 이미 방문한 곳이 아니라면 dq에 추가
                    if place[nx][ny] != "X" && !visited[nx][ny] {
                        toGo.append([nx, ny, nc])
                        visited[nx][ny] = true
                    }
                }
            }
        }
    } 
    
    // 전부 다 지켰다면 1 return
    return 1
}