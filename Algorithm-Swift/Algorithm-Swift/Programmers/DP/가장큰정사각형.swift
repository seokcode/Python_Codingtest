//
//  가장큰정사각형.swift
//  Algorithm-Swift
//
//  Created by 이원석 on 2021/03/18.
//
import Foundation

func solution(_ board:[[Int]]) -> Int
{
    let width = board[0].count
    let height = board.count
    var copy = board.map{$0.map{$0}};
    var answer = 0

    for i in 1..<height {
        for j in 1..<width {
          if copy[i][j] == 1{
            copy[i][j] = min(copy[i][j-1], min(copy[i-1][j],copy[i-1][j-1]))+1
          }
        }
    }
    
    for i in 0..<height {
        for j in 0..<width {
            if copy[i][j] >= answer{
                answer = copy[i][j]
            }
        }
    }
    
    return answer*answer
}
