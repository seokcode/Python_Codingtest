# DFS와 BFS
> **Silver 2**
>
> **2021-05-23**
>
> [B1260](https://www.acmicpc.net/problem/1260)

## Sol

문제
```xml
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.
```

입력
```xml
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.
```

출력
```xml
첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.
```


## 답안
```swift
let nm = readLine()!.split(separator: " ").map{Int(String($0))!}
let n = nm[0]
let m = nm[1]
let startNode = nm[2]

var node:[[Int]] = [[0]]
for i in 1...n {
    node.append([i])
}
for _ in 1...m {
    let line = readLine()!.split(separator: " ").map{Int(String($0))!}
    node[line[0]].append(line[1])
    node[line[1]].append(line[0])
}

print(DFS(n: n, start: startNode, node: node))
print(BFS(n: n, start: startNode, node: node))

func BFS(n: Int, start: Int, node: [[Int]]) -> String {
    var queue:[Int] = []
    var isVisited = Array(repeating: false, count: n+1)
    var result = "\(start) "
    isVisited[start] = true
    queue.append(start)
    
    while !queue.isEmpty {
        let next = queue.removeFirst()
        for i in node[next].sorted() {
            if !isVisited[i] {
                queue.append(i)
                isVisited[i] = true
                result += "\(i) "
            }
        }
    }
    return result
}

func DFS(n: Int, start: Int, node: [[Int]]) -> String {
    var stack:[Int] = []
    var isVisited = Array(repeating: false, count: n+1)
    var result = ""
    stack.append(start)
    
    func depthSearch() {
        let next = stack.removeLast()
        isVisited[next] = true
        result += "\(next) "
        for i in node[next].sorted() {
            if !isVisited[i] {
                stack.append(i)
                depthSearch()
            }
        }
    }
    depthSearch()
    return result
}
```