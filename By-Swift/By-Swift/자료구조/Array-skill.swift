import Foundation

var arr = [[Int]]()

arr = [[1,2,10],[342,213,22],[29,1231,2]]
print("Array => \n \(arr) \n")

for (idx,var i) in arr.enumerated(){
  i.sort(by: <)
  arr[idx] = i
}
print("2차원 배열 내 요소 오름차순 정렬 \n \(arr) \n")

var new = [Int]()
arr.forEach{new += $0.filter{$0 >= 10}}
print("2차원 배열 내 요소 10이상만 걸러서 1차원 배열로 만들기 \n \(new) \n")

var newb = [[Int]]()
var idx = 0
arr.forEach{newb.append($0.filter{$0 >= 10})}
print("2차원 배열 내 요소 10이상만 거르기 \n \(newb) \n")


arr = [[1,2,10],[342,213,22],[29,1231,2]]
var turn = [[Int]]()
for i in 0..<arr.count{
  turn.append([arr[0][i],arr[1][i],arr[2][i]])
}
print("2차원 배열 내 요소 오른쪽으로 90도 돌리기 \n \(turn) \n")

