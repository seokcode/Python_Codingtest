//
//  기능개발.swift
//  Algorithm-Swift
//
//  Created by 이원석 on 2021/04/21.
//
import Foundation

func solution(_ progresses:[Int], _ speeds:[Int]) -> [Int] {  
    var result: [Int] = []
    var count = 0
    
    let times = zip(progresses,speeds).map({ (num: Int, time: Int) -> Int in
        if (100-num)%time == 0{
          return (100-num)/time
        }else{
          return ((100-num)/time)+1
        }
    })
    
    var flag = times[0]
    times.forEach{
      if flag >= $0{
        count += 1
      }else{
        result.append(count)
        flag = $0
        count = 1
      }
    }
    result.append(count)
   
   return result
   
}