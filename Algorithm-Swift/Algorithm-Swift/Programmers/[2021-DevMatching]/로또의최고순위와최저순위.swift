//
//  로또의 최고순위와 최저순위.swift
//  Algorithm-Swift
//
//  Created by 이원석 on 2021/05/09.
//

import Foundation

func solution(_ lottos:[Int], _ win_nums:[Int]) -> [Int] {
    let rank = [6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6]
    var correct = 0
    var zero = 0
    lottos.forEach{
        if win_nums.contains($0){ correct += 1}
        else if $0 == 0 { zero += 1}
    }
    return [rank[correct+zero]!, rank[correct]!]
}

