//
//  주식.swift
//  Algorithm-Swift
//
//  Created by 이원석 on 2021/03/17.
//

import Foundation

let T = Int(readLine()!)!

for _ in 0..<T {
  let days = Int(readLine()!)!
  let stocks = readLine()!.split(separator: " ").map{Int(String($0))!}

  var answer = 0
  var max_cost = stocks.last

  for i in (0..<days-1).reversed(){
    if stocks[i] > max_cost! {
      max_cost! = stocks[i]
    }else{
      answer += (max_cost!-stocks[i])
    }
  }
  print(answer)
}
