/* 
[링크](https://github.com/raywenderlich/swift-algorithm-club/tree/master/Merge%20Sort)
머지소트는 이미 정렬이 되어 있던 말던 똑같은 작업을 수행하기 떄문에
최고, 평균, 최악 시간 복잡도: O(n log n) 이다.

단점은 배열의 크기만큼 일을 해야한다는 것이다. 퀵소트와의 차이점이다.

분할 정복으로 소팅
Top-down은 먼저 배열을 더 작은 배열로 쪼개고 합쳐야해서 잘 사용되지 않음
Bottpm-Up은 쪼개는 과정을 생략하고 바로 배열의 각 인덱스를 비교하여 머지가 이루어지기 때문에 간편
*/

// Top-down
func mergeSort(_ array: [Int]) -> [Int] {
    guard array.count > 1 else { return array } // 1

    let middleIndex = array.count / 2 // 2

    let leftArray = mergeSort(Array(array[0..<middleIndex])) // 3
    let rightArray = mergeSort(Array(array[middleIndex..<array.count])) // 4

    return merge(leftPile: leftArray, rightPile: rightArray) // 5
}

func merge(leftPile: [Int], rightPile: [Int]) -> [Int] {
    var leftIndex = 0
    var rightIndex = 0

    var orderedPile = [Int]()
    orderedPile.reserveCapacity(leftPile.count + rightPile.count)

    while leftIndex < leftPile.count && rightIndex < rightPile.count {
        if leftPile[leftIndex] < rightPile[rightIndex] {
            orderedPile.append(leftPile[leftIndex])
            leftIndex += 1
        } else if leftPile[leftIndex] > rightPile[rightIndex] {
            orderedPile.append(rightPile[rightIndex])
            rightIndex += 1
        } else {
            orderedPile.append(leftPile[leftIndex])
            leftIndex += 1
            orderedPile.append(rightPile[rightIndex])
            rightIndex += 1
        }
    }

    while leftIndex < leftPile.count {
        orderedPile.append(leftPile[leftIndex])
        leftIndex += 1
    }

    while rightIndex < rightPile.count {
        orderedPile.append(rightPile[rightIndex])
        rightIndex += 1
    }

    return orderedPile
}



// Bottom-Up
func mergeSortBottomUp<T>(_ a: [T], _ isOrderedBefore: (T, T) -> Bool) -> [T] {
  let n = a.count

  var z = [a, a]      // 1
  var d = 0

  var width = 1
  while width < n {   // 2

    var i = 0
    while i < n {     // 3

      var j = i
      var l = i
      var r = i + width

      let lmax = min(l + width, n)
      let rmax = min(r + width, n)

      while l < lmax && r < rmax {                // 4
        if isOrderedBefore(z[d][l], z[d][r]) {
          z[1 - d][j] = z[d][l]
          l += 1
        } else {
          z[1 - d][j] = z[d][r]
          r += 1
        }
        j += 1
      }
      while l < lmax {
        z[1 - d][j] = z[d][l]
        j += 1
        l += 1
      }
      while r < rmax {
        z[1 - d][j] = z[d][r]
        j += 1
        r += 1
      }

      i += width*2
    }

    width *= 2
    d = 1 - d      // 5
  }
  return z[d]
}


let array = [2, 1, 5, 4, 9]
mergeSortBottomUp(array, <) // [1, 2, 4, 5, 9]
