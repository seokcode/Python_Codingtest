//
//  괄호회전하기.swift
//  Algorithm-Swift
//
//  Created by 이원석 on 2021/04/19.
//

import Foundation

func rotation(_ arr: Array<Character>) -> Array<Character> {
    var arr = arr
    arr.append(arr[0])
    arr.removeFirst()
    
    return arr
}

func check(_ arr: Array<Character>,_ dic: Dictionary<String,String>) -> Bool {
    var stack: [String] = []
    
    for i in arr{
        let i = String(i)
        if ["[","{","("].contains(i){
            stack.append(i)
        }else if !stack.isEmpty {
            if stack.popLast() != dic[i]{
                return false
            }            
        }else{
            return false
        }
    }
    
    if stack.isEmpty {
        return true
    }
    
    return false
}

func solution(_ s:String) -> Int {
    var answer = 0
    var ros = Array(s)
    let d = ["]":"[", "}":"{", ")":"("]
    
    for _ in 0..<s.count{        
        if check(ros, d){
            answer += 1
        }
        ros = rotation(ros)
    }
    
    return answer
}