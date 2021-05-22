//
//  DFS와BFS.swift
//  Algorithm-Swift
//
//  Created by 이원석 on 2021/05/23.
//

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