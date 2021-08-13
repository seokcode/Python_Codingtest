import Foundation

let input = readLine()!.split{$0==" "}.map{Int(String($0))!}
let N = input[0], M = input[1]
let treeArr = readLine()!.split{$0==" "}.map{Int(String($0))!}

var start = 1
var end = treeArr.max()!

while start <= end {
    let mid = (start+end)/2  
    var length = 0
    for i in 0..<N {
      if treeArr[i] > mid {
        length += (treeArr[i] - mid)
      }
    }

    if length >= M {
        start = mid + 1
    } else {
        end = mid - 1
    }
}

print(end)