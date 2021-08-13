//
//  쉬운계단수.swift
//  Algorithm-Swift
//
//  Created by 이원석 on 2021/05/23.
//

import Foundation

// D[N][L]: 길이가 N이고 마지막 수가 L인 수
// D[N][L] = D[N-1][L-1] + D[N-1][L+1]
let mod = 1000000000
let n = Int(readLine()!)!
var arr = Array(repeating: Array(repeating: 0, count: 10), count: 101)
for i in 1...9 {
  arr[1][i] = 1
}

for i in 2..<n+1 {
  for j in 0...9 {
    arr[i][j] = 0
    if j-1 >= 0 {
      arr[i][j] += arr[i-1][j-1]
    }
    if j+1 <= 9 {
      arr[i][j] += arr[i-1][j+1]
    }
    arr[i][j] %= mod
  }
}

print((arr[n].reduce(0){$0+$1})%mod)