//
//  K번째수.swift
//  Algorithm-Swift
//
//  Created by 이원석 on 2021/04/19.
//


import Foundation

func solution(_ array:[Int], _ commands:[[Int]]) -> [Int] {
    return commands.map({(key)in 
            return array[(key[0]-1)...(key[1]-1)].sorted()[key[2]-1]                  
    })
    
}