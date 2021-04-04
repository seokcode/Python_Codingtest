//
//  피보나치수.swift
//  Algorithm-Swift
//
//  Created by 이원석 on 2021/04/04.
//

func solution(_ n:Int) -> Int {
    var arr = [Int](repeating: 0, count: n+1)
    arr[0] = 0
    arr[1] = 1
    
    if n < 2 { return arr[n] }
    
    for i in 2..<n+1{
        arr[i] = (arr[i-1]+arr[i-2])%1234567
    }
    
    return arr[n]
}
