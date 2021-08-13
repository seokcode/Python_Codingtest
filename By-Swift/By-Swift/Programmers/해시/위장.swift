//
//  위장.swift
//  Algorithm-Swift
//
//  Created by 이원석 on 2021/03/11.
//

// [고득점Kit]해시 - 위장

import Foundation

func arrangeClothes(clothes:[[String]]) -> [String: [String]] {

    var dict: [String: [String]] = [:]
    clothes.forEach { item in
        let value = item[0]
        let key = item[1]

        if let existClothes = dict[key] {
          dict[key] = existClothes + [value]
        }
        else {
          dict[key] = [value]
        }
    }
    return dict
}

func solution(_ clothes:[[String]]) -> Int {
    let arranged = arrangeClothes(clothes: clothes)
    var count = 1
    
    arranged.forEach {
        count *= ($0.value.count + 1)
    }
    return count-1
}
