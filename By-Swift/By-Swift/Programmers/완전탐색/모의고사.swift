//
//  완전탐색.swift
//  Algorithm-Swift
//
//  Created by 이원석 on 2021/04/09.
//

import Foundation

func solution(_ answers:[Int]) -> [Int] {
    var result:[Int] = []
    let first = [1,2,3,4,5]
    let second = [2,1,2,3,2,4,2,5]
    let third = [3,3,1,1,2,2,4,4,5,5]
    var correct = [0,0,0]
    
    for i in 0..<answers.count{
        if answers[i] == first[i % first.count]{
            correct[0] += 1
        }
        if answers[i] == second[i % second.count]{
            correct[1] += 1
        }
        if answers[i] == third[i % third.count]{
            correct[2] += 1
        }
    }
    for (idx,j) in correct.enumerated() {
        if j == correct.max(){
          result.append(idx+1)
        }
        
    }
    
    return result
}
