let n = Int(readLine()!)!
let limit = 100000
let mod = 1000000009
var d = Array(repeating: Array(repeating: 0, count: 4), count: limit+1)

for i in 1...limit {
  if i-1 >= 0 {
    d[i][1] = d[i-1][2] + d[i-1][3]
    if i == 1 {
      d[i][1] = 1 
      // 1로 끝나면서 1을 만들 수 있는건 {1} 한가지
    }
    d[i][1] %= mod
  }
  if i-2 >= 0 {
    d[i][2] = d[i-2][1] + d[i-2][3]
    if i == 2 {
      d[i][2] = 1 
      // 2로 끝나면서 2를 만들 수 있는건 {2} 한가지
    }
    d[i][2] %= mod
  }
  if i-3 >= 0 {
    d[i][3] = d[i-3][1] + d[i-3][2]
    if i == 3 {
      d[i][3] = 1 
      // 3으로 끝나면서 3을 만들 수 있는건 {3} 한가지
    }
    d[i][3] %= mod
  }
}

for _ in 0..<n {
  let num = Int(readLine()!)!
  print((d[num].reduce(0){$0+$1})%mod)
}