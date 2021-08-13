//
//  오픈채팅방.swift
//  Algorithm-Swift
//
//  Created by 이원석 on 2021/04/16.
//
import Foundation

func solution(_ record:[String]) -> [String] {
    var action = ["Enter": "님이 들어왔습니다.", "Leave": "님이 나갔습니다."]
    var result = [String]()
    var d = [String: String]()

    for r in record{
        var rec = r.components(separatedBy : " ")
        if rec[0] == "Change" || rec[0] == "Enter"{
            d[rec[1]] = rec[2]   
        }
    }

    for r in record{
        var rec = r.components(separatedBy : " ")

        if rec[0] != "Change"{
            result.append("\(d[rec[1]]!)"+"\(action[rec[0]]!)")
        }
    }

    return result
}


// 다른사람 풀이
/*
import Foundation

func solution(_ record:[String]) -> [String] {
    let actions = ["Enter":"님이 들어왔습니다.", "Leave":"님이 나갔습니다."]
    var a = [String:String]()

    record.forEach {
        let separated = $0.components(separatedBy: " ")
        if separated.count > 2 {
            a[separated[1]] = separated[2]
        }
    }

    return record.filter { !$0.contains("Change") }.map { (value:String) -> String in
        let separated = value.components(separatedBy: " ")
        let newString = a[separated[1]]! + actions[separated[0]]!
        return newString
    }
}
*/