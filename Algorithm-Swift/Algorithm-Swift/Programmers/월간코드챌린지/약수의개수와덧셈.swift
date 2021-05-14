//
//  약수의개수와덧셈.swift
//  Algorithm-Swift
//
//  Created by 이원석 on 2021/05/15.
// 
import Foundation

func solution(_ left:Int, _ right:Int) -> Int {
    var answer = 0
    
    for number in left...right{
        if floor(sqrt(Double(number))) == sqrt(Double(number)) {
            answer -= number
        } else {
            answer += number
        }
    }
    return answer
}