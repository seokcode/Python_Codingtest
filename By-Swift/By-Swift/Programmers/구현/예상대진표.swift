//
//  예상대진표.swift
//  Algorithm-Swift
//
//  Created by 이원석 on 2021/05/23.
//

import Foundation

func solution(_ n:Int, _ a:Int, _ b:Int) -> Int
{
    var answer = 0
    var p1 = a
    var p2 = b
    
    while p1 != p2 {
        p1 = (p1+1)/2
        p2 = (p2+1)/2
        answer += 1
    }
    
    return answer
}