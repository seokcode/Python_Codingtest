//
//  사칙연산.swift
//  Algorithm-Swift
//
//  Created by 이원석 on 2021/03/07.
//

let lineArr = readLine()!.split(separator: " ").map{ return Int($0)! }

print("\(lineArr[0] + lineArr[1])")
print("\(lineArr[0] - lineArr[1])")
print("\(lineArr[0] * lineArr[1])")
print("\(lineArr[0] / lineArr[1])")
print("\(lineArr[0] % lineArr[1])")
