//
//  삼각달팽이.swift
//  Algorithm-Swift
//
//  Created by 이원석 on 2021/05/08.
//

import Foundation

func solution(_ n:Int) -> [Int] {
    var nums = Array(repeating: Array(repeating: 0, count: n), count: n+1)
    // 밑, 오, 왼대
    var x = 0
    var y = 0
    var count = 1
    let direction = [[1,0],[0,1],[-1,-1]]
    for i in 0..<n{
        for _ in i..<n{
            x += direction[i%3][0]
            y += direction[i%3][1]
            nums[x][y] = count
            count += 1
        }
    }
    
    return nums.flatMap{ $0.filter{ $0 > 0}}
}