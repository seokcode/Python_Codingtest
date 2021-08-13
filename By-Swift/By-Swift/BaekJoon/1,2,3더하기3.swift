let n = Int(readLine()!)!
var d = Array(repeating: 0, count: 1000001)
d[0] = 1
d[1] = 1
d[2] = 2
d[3] = 4

var before = 3
for _ in 0..<n {
  let num = Int(readLine()!)!
  if d[num] == 0 {
    for j in before...num {
      d[j] = d[j-1] + d[j-2] + d[j-3]
      d[j] %= 1000000009
    }
    before = num
  }
  print(d[num])
}