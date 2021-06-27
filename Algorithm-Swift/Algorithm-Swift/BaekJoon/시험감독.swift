import Foundation

let num = Int(readLine()!)!
let applier = readLine()!.split(separator: " ").map{Int(String($0))!}
let ability = readLine()!.split(separator: " ").map{Int(String($0))!}
var answer = 0

for i in 0..<num {
  if applier[i] <= ability[0] {
    answer += 1
  } else {
    answer += Int(ceil(Float(applier[i]-ability[0])/Float(ability[1])))+1
  }
}
print(answer)