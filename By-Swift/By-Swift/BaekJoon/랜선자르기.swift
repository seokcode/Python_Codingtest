import Foundation

let input = readLine()!.split{$0==" "}.map{Int(String($0))!}
let K = input[0], N = input[1]
var lanList: [Int] = []

for _ in 0..<K {
  lanList.append(Int(readLine()!)!)
}

var start = 1
var end = lanList.max()!

while start <= end {
    let mid = (start+end)/2  
    var count = 0
    for i in 0..<K {
        count += lanList[i]/mid
    }

    if count >= N {
        start = mid + 1
    } else {
        end = mid - 1
    }
}

print(end)