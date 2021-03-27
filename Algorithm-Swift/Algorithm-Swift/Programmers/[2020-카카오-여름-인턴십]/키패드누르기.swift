//
//  키패드누르기.swift
//  Algorithm-Swift
//
//  Created by 이원석 on 2021/03/23.
//
import Foundation

func solution(_ numbers:[Int], _ hand:String) -> String {
    var left : Int = 10
    var right: Int = 12
    var answer : Array<String> = []
    for var i in numbers{
        if i == 0 {
            i = 11
        }
        if i == 1 || i == 4 || i == 7{
            answer.append("L")
            left = i
        }else if i == 3 || i == 6 || i == 9{
            answer.append("R")
            right = i
        }
        else{
            let dl = (abs(left-i)/3)+(abs(left-i)%3)
            let dr = (abs(right-i)/3)+(abs(right-i)%3)
            if dl > dr {
                answer.append("R")
                right = i
            }else if dl == dr {
                if hand == "right"{
                    answer.append("R")
                    right = i
                }else{
                    answer.append("L")
                    left = i
                }
            }else{
                answer.append("L")
                left = i
            }
        }
    }
    
    return answer.joined(separator: "")
}
