//
//  실패율.swift
//  Algorithm-Swift
//
//  Created by 이원석 on 2021/04/16.
//
import Foundation

func solution(_ N:Int, _ stages:[Int]) -> [Int] {
    var failure = [Int:Double]()
    var people = stages.count
    
    for i in 0..<N{
      let fail = stages.filter{$0 == i+1}.count
      failure[i] = Double(fail) / Double(people)
      people -= fail
    }
    
    let answer = failure.sorted(by: <).sorted{$0.value > $1.value}.map{$0.key+1} 
    return answer
}