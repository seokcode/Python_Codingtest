func sosu(_ num: Int) -> Bool {
  var t = 2
  while t * t <= num {
    if num % t == 0 {
      return false
    }
    t += 1
  }
  return true
}

func saangn(_ num: Int,_ visited: [Int]) -> Bool {
  var result = 0
  var visited = visited
  let splitNum = Array(String(num))
  
  for i in splitNum {
    result += Int(String(i))! * Int(String(i))!
  }
  if result == 1 {
    return true
  } else if visited.contains(result) {
    return false
  }
  visited.append(result)
  return saangn(result, visited)
}

let n = Int(readLine()!)!

for i in 2...n {
  let visited: [Int] = []
  if sosu(i) && saangn(i,visited){
    print(i)
  }
}