//
//  짝지어제거하기.swift
//  Algorithm-Swift
//
//  Created by 이원석 on 2021/05/23.

import Foundation

func solution(_ s:String) -> Int{
    var arr = Array(s)
    var temp = [Character]()
    
    for i in arr.indices {
        if temp.isEmpty {
            temp.append(arr[i])
        } else {
            if temp.last! == arr[i] {
                temp.removeLast()
            } else {
                temp.append(arr[i])      
            }
        }
    }

    return temp.isEmpty ? 1 : 0
}