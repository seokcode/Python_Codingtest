//
//  단어변환.swift
//  Algorithm-Swift
//
//  Created by 이원석 on 2021/04/23.
//

import Foundation

func solution(_ begin:String, _ target:String, _ words:[String]) -> Int {
    var check = Array(repeating: false, count: words.count)
    var possible = [begin]
    var candidate: [String] = []
    var answer = 0
    
    if !words.contains(target){
        return 0
    }
    
    while check.filter({ !$0 }).count != 0 {
        for (idx,i) in words.enumerated(){
            if !check[idx]{
                let temp1 = Array(i)
                for j in possible{
                    var count = 0
                    let temp2 = Array(j)
                    for k in 0..<begin.count{
                        if temp1[k] == temp2[k]{
                            count += 1
                        }
                        if count == begin.count-1{
                            check[idx] = true
                            candidate.append(i)
                        }
                    }
                }
            }
        }
        answer += 1
        if candidate.contains(target){
            return answer
        }else{
            possible = candidate
        }
    }
    
    return 0
}