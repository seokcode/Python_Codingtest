//
//  영어끝말잇기.swift
//  Algorithm-Swift
//
//  Created by 이원석 on 2021/05/12.
//
import Foundation

func solution(_ n:Int, _ words:[String]) -> [Int] {
    var person = Array(repeating: 0, count: n)
    var storage = [String]()
    
    for (idx,w) in words.enumerated() {
        person[idx%n] += 1
        if !storage.isEmpty {
            if storage.contains(w) || Array(storage.last!).last != Array(w).first{
                return [(idx%n)+1, person[idx%n]]
            }
        }
        storage.append(w)
    }
    return [0,0]
}