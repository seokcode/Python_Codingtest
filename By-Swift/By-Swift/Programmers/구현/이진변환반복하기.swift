//
//  이진변환반복하기.swift
//  Algorithm-Swift
//
//  Created by 이원석 on 2021/04/04.
//

import Foundation

func solution(_ s:String) -> [Int] {
    var zero: Int = 0
    var count: Int = 0
    var copy_s = s
    
    while copy_s != "1"{
        let current_zero = copy_s.replacingOccurrences(of: "0", with: "").count
        zero += copy_s.count - current_zero
        copy_s = String(current_zero, radix: 2)
        count += 1
    }
    return [count, zero]
}
