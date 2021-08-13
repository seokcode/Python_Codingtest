//
//  네트워크.swift
//  Algorithm-Swift
//
//  Created by 이원석 on 2021/04/23.
//

import Foundation

func solution(_ n:Int, _ computers:[[Int]]) -> Int {
    var visited = Array(repeating: false, count: n)
    var answer = 0
    
    func dfs(_ idx: Int){
        visited[idx] = true
        for (i,connect) in computers[idx].enumerated(){
            if i != idx && connect == 1 && !visited[i]{
                    dfs(i)
                }
            }
        return
    }

    for j in 0..<n{
        if !visited[j]{
            dfs(j)
            answer += 1
        }       
    }
    return answer
}