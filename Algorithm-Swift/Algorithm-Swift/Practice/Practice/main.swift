//
//  main.swift
//  Practice
//
//  Created by 이원석 on 2021/04/16.
//

import Foundation

let numbers: [Int] = [1,2,3,4]
let reversed: [Int]

reversed = numbers.sorted(by: { (left:Int, right: Int) -> Bool in
    return left > right})

print(reversed) //[4,3,2,1]

