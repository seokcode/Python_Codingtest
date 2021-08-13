import Foundation

func solution(_ numbers:[Int]) -> String { 
    let sortedNumbers = numbers.sorted{ Int("\($0)\($1)")! > Int("\($1)\($0)")! }
    return sortedNumbers.reduce(0){$0+$1} == 0 ? "0" : sortedNumbers.reduce(""){"\($0)\($1)"}
}