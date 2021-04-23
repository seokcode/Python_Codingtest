//
//  타겟넘버.swift
//  Algorithm-Swift
//
//  Created by 이원석 on 2021/04/23.
//

import Foundation

var answer = 0

func dfs(_ idx: Int,_ current: Int,_ numbers: [Int], _ target: Int) -> Int{
        var answer = 0
        if idx == numbers.count{
            return current == target ? 1:0
        }else{
            for i in [1,-1]{
                answer += dfs(idx+1,current+(i*numbers[idx]),numbers, target)
            }
            return answer
        }
    }

func solution(_ numbers:[Int], _ target:Int) -> Int {
       
    return dfs(0,0,numbers,target)
}