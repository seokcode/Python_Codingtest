//
//  프린터.swift
//  Algorithm-Swift
//
//  Created by 이원석 on 2021/04/21.
//
import Foundation

func solution(_ priorities:[Int], _ location:Int) -> Int {
    var cp : [[Int]] = []
    var count = 0
    for (idx,i) in priorities.enumerated() {
      cp.append([idx,i])
    }
    print(cp)
    
    while cp.count > 0 {
        if cp.contains(where: { $0[1] > cp[0][1]}){
            let temp = cp.removeFirst()
            cp.append(temp)
        }else{
            let idx = cp[0][0]
            cp.removeFirst()
            count += 1
            
            if idx == location{
                return count
            }
        }

    }
    
    return 0
}