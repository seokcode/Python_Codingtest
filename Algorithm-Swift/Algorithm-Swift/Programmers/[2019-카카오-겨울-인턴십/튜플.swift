//
//  튜플.swift
//  Algorithm-Swift
//
//  Created by 이원석 on 2021/03/27.
//

// 차집합 풀이
func solution(_ s:String) -> [Int] {
    var result = [Int]()
    var sets = s.split(omittingEmptySubsequences: true, whereSeparator: { "}".contains($0) }).map {
        $0.split(omittingEmptySubsequences: true, whereSeparator: { "{,".contains($0) }).map { Int($0)! }
    }
    // print(sets) //[[2], [2, 1], [2, 1, 3], [2, 1, 3, 4]]

    sets.sort { (lhs, rhs) -> Bool in
        lhs.count < rhs.count
    }

    sets.forEach {
        // 차집합
        result.append((Set($0).subtracting(result)).first!)
    }

   return result
}

// 딕셔너리 풀이
import Foundation

func solution(_ s:String) -> [Int] {
    var result = [Int]()
    let sets = s.split(omittingEmptySubsequences: true, whereSeparator: { "}".contains($0) }).map {
        $0.split(omittingEmptySubsequences: true, whereSeparator: { "{,".contains($0) }).map { Int($0)! }
    }.sorted{ (ele1, ele2) -> Bool in
        return ele1.count < ele2.count
    }
    // print(sets) //[[2], [2, 1], [2, 1, 3], [2, 1, 3, 4]]

    var dict = [Int : Int]()

    for i in sets{
      for j in i{
        if dict[j] == nil {
          result.append(j)
          dict[j] = 1
        }
      }
    }

   print(result)
   return result
}
