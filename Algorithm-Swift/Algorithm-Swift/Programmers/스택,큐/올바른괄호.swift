//
//  올바른괄호.swift
//  Algorithm-Swift
//
//  Created by 이원석 on 2021/03/20.
//
import Foundation

func solution(_ s:String) -> Bool
{
    var count : Int = 0
    for i in s{
        if i == "("{
            count += 1
        }else{
            count -= 1
        }
        
        if count < 0 {
            return false
        }
    }
    
    if count > 0 {
        return false
    }

    return true
}
