//
//  입국심사.swift
//  Algorithm-Swift
//
//  Created by 이원석 on 2021/04/30.
//
import Foundation

func solution(_ n:Int, _ times: [Int]) -> Int64 {
    guard let tms = times.max() else {return 0}
    var minimum = 1
    var maximum = tms*n
    var answer = 0
    
    while minimum <= maximum {
        let avg = (minimum+maximum)/2
        var count = 0
        for i in times{
            count += avg/i
            if count >= n {break}
        }
        
        if count >= n{
            answer = avg
            maximum = avg - 1
        }else{
            minimum = avg + 1
        }
    }
    return Int64(answer)
}


import Foundation

func solution(_ n:Int, _ times: [Int]) -> Int64 {
    guard let tms = times.max() else {return 0}
    var minimum = 1
    var maximum = (tms*n)
    var answer = 0
    
    while minimum <= maximum {
        let avg = (minimum+maximum)/2
        let count = times.reduce(0){$0 + (avg/$1)}
        
        if count >= n{
            answer = avg
            maximum = avg - 1
        }else{
            minimum = avg + 1
        }
    }
    return Int64(answer)
}