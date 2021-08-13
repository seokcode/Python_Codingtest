//
//  음양더하기.swift
//  Algorithm-Swift
//
//  Created by 이원석 on 2021/04/16.
//

// 내코드
import Foundation

func solution(_ absolutes:[Int], _ signs:[Bool]) -> Int {
    let merge = zip(absolutes,signs)
    var answer = 0

    merge.forEach {
        if $1 {
            answer += $0
        }else{
            answer -= $0   
        }
    }

    return answer
}

// 더 빠른 코드
import Foundation

func solution(_ absolutes:[Int], _ signs:[Bool]) -> Int {
    var answer = 0

    for i in 0..<signs.count {
        answer += signs[i] == true ? absolutes[i] : -absolutes[i]
    }

    return answer
}
