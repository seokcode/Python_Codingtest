//
//  group-anagrams.swift
//  Algorithm-Swift
//
//  Created by 이원석 on 2021/03/25.
//


// 내 풀이
class Solution {
    func groupAnagrams(_ strs: [String]) -> [[String]] {
        var dict: [String: [String]] = [:]
        var answer: [[String]] = []
        for anagram in strs{
            var temp = Array(anagram)
            temp = temp.sorted()
            var list = temp.map { String($0) }.joined(separator:"")
            if let exist = dict[list] {
              dict[list] = exist + [anagram]
            }
            else {
              dict[list] = [anagram]
            }
       }
        
        dict.forEach {
            answer.append($0.value)
        }
        return answer
    }
}

// 다른 사람 풀이
class Solution {
    func groupAnagrams(_ strs: [String]) -> [[String]] {
         if strs.count == 0 { return [[""]] }
         var dict = [String:[String]]()
        
        var res = [[String]]()
        for str in strs {
            dict[String(str.sorted()), default:[]].append(str)
        }
        
        for anagrams in dict.values {
            res.append(anagrams)
        }
        
        return res
    }
}
