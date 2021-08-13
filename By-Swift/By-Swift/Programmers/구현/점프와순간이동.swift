//
//  점프와순간이동.swift
//  Algorithm-Swift
//
//  Created by 이원석 on 2021/05/16.
//
import Foundation

func solution(_ n:Int) -> Int 
{
    var answer = 0
    var num = n
    
    while num != 0 {
        if num % 2 != 0 {
            answer += 1
            num -= 1
        } else {
            num /= 2
        }
    }
    
    return answer
}