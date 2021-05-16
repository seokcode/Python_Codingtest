//
//  최댓값과최솟값.swift
//  Algorithm-Swift
//
//  Created by 이원석 on 2021/05/16.
//

func solution(_ s:String) -> String {
    let answer = Array(s).split(separator: " ").compactMap{Int($0)}
    return "\(answer.min()!) \(answer.max()!)" 
}