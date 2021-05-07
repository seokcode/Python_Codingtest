//
//  스킬트리.swift
//  Algorithm-Swift
//
//  Created by 이원석 on 2021/05/07.
//
import Foundation

func check(_ custom: [Character], _ preceded: [Character]) -> Bool{
    var temp = [Character]()
    for i in custom{
        if preceded.contains(i){
            if preceded[(temp.count) % preceded.count] != i{
                return false   
            }
            temp.append(i)
        }
    }
    return true
}

func solution(_ skill:String, _ skill_trees:[String]) -> Int {
    var answer = 0
    let preceded = Array(skill)
    
    for i in skill_trees{
        let custom = Array(i)
        if check(custom, preceded){
            answer += 1
        }
    }
    return answer
}