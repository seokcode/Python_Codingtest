//
//  main.swift
//  Practice
//
//  Created by 이원석 on 2021/04/16.
//

//import Foundation
//
//let numbers: [Int] = [1,2,3,4]
//let reversed: [Int]
//
//reversed = numbers.sorted(by: { (left:Int, right: Int) -> Bool in
//    return left > right})
//
//print(reversed) //[4,3,2,1]

//let someNumbers: [Int] = [2, 8, 15,20]
//
//// 초깃값이 0이고 someNumbers 내부의 모든 값을 더합니다.
//let sum: Int = someNumbers.reduce(0, { (first: Int, second: Int) -> Int in
//    //print("\(first) + \(second)")
//        // 0+2
//        // 2+8
//        // 10+15
//    return first + second
//})
//
//print(sum)  // 25
//
//// 초깃값이 0이고 someNumbers 내부의 모든 값을 뺍니다.
//var subtract: Int = someNumbers.reduce(0, { (first: Int, second: Int) -> Int in
//    print("\(first) - \(second)") //어떻게 동작하는지 확인해보세요
//    return first - second
//})
//
//print(subtract) // -25
//
//// 초깃값이 3이고 someNumbers 내부의 모든 값을 더합니다.
//let sumFromThree = someNumbers.reduce(3) { $0 + $1 }
//
//print(sumFromThree) // 28


//let numbers = [1:10,2:20,3:30,4:40]
//
//let mapped = numbers.map { Array(repeating: $0.key, count: $0.key) }
//print(mapped)
//let flatMapped = numbers.flatMap { Array(repeating: $0.key, count: $0.key) }
//print(flatMapped)
//
//let scores = [[5,2,7], [4,8], [9,1,3]]
//let allScores = scores.flatMap { $0 } // [5, 2, 7, 4, 8, 9, 1, 3]
//let passMarks = scores.flatMap { $0.filter { $0 > 5} } // [7, 8, 9]

//let array: [[Int?]] = [[1, 2, 3], [nil, 5], [6, nil], [nil, nil]]
//let cmapTest = array.compactMap{ $0 }
//let fmapcmapMap = array.flatMap { $0 }.compactMap{ $0 }
//
//print(cmapTest)
//print(fmapcmapMap)

//let array = [1,2,nil,10,123,nil,nil]
//let cmapTest = array.compactMap{ $0 } //[1, 2, 10, 123]
//
//print(cmapTest)
//


let numbers = [1,2,3,4,5]

numbers.forEach {
    if $0 % 2 == 0{
        return
    }else{
        print($0)
    }
}
