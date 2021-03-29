//
//  땅따먹기.swift
//  Algorithm-Swift
//
//  Created by 이원석 on 2021/03/29.
//
import Foundation

func solution(_ land:[[Int]]) -> Int{
    let l = land.count-1
    var land = land
    for i in 0..<l {
        land[i+1][0] += max(land[i][1],land[i][2],land[i][3])
        land[i+1][1] += max(land[i][0],land[i][2],land[i][3])
        land[i+1][2] += max(land[i][1],land[i][0],land[i][3])
        land[i+1][3] += max(land[i][1],land[i][2],land[i][0])
    }

    return max(land[l][0],land[l][1],land[l][2],land[l][3])
}
