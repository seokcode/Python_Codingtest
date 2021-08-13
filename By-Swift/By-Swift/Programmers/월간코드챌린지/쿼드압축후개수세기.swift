//
//  쿼드압축후개수세기.swift
//  Algorithm-Swift
//
//  Created by 이원석 on 2021/03/28.
//
import Foundation

func solution(_ arr:[[Int]]) -> [Int] {
    var answer : Array<Int> = [0,0]
    
    func divide(_ x: Int, _ y: Int, _ n: Int) {
        let flag = arr[x][y]
        for i in x..<x+n {
            for j in y..<y+n{
                if arr[i][j] != flag{
                    let here = n/2
                    divide(x, y, here)
                    divide(x+here, y, here)
                    divide(x, y+here, here)
                    divide(x+here, y+here, here)
                    return
                }
            }
        }
        answer[flag] += 1
    }
    
    divide(0,0,arr.count)
    return answer
}
