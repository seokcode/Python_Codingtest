//
//  다음큰숫자.swift
//  Algorithm-Swift
//
//  Created by 이원석 on 2021/04/10.
//

import Foundation

func getOne(_ binary: String) -> Int{
  return Array(binary).filter{$0 == "1"}.count
}

func solution(_ n:Int) -> Int
{
    var num = n
    let counter = String(n, radix:2)

    while true{
      num += 1
      if getOne(counter) == getOne(String(num,radix:2)){
        break
      }
    }

    return num
}