/*
[링크](https://github.com/raywenderlich/swift-algorithm-club/tree/master/Insertion%20Sort)
시간복잡도 최악: O(n^2), 평균: O(n^2)
input이 많아질수록 퀵소트나 머지소트(O(n log n)와의 상대적인 시간복잡도가 체감될 것이다.
*/

// ver.1
func insertionSort_ver1(_ array: [Int]) -> [Int] {
    var sortedArray = array
    for index in 1..<sortedArray.count {
        var curIdx = index
        while curIdx > 0 && sortedArray[curIdx] < sortedArray[curIdx-1] {
            sortedArray.swapAt(curIdx-1, curIdx)
            curIdx -= 1
        }
    }
    return sortedArray
}

// ver.2 
// ver.1에서 swap을 매번 수행하지 않고 본인 숫자를 복사하여 가지고 있다가 자신보다 작은 숫자가 없을 때 한번만 삽입
func insertionSort_ver2(_ array: [Int]) -> [Int] {
    var sortedArray = array
    for index in 1..<sortedArray.count {
        var curIdx = index
        let temp = sortedArray[curIdx]
        while curIdx > 0 && sortedArray[curIdx] < sortedArray[curIdx-1] {
            sortedArray[curIdx] = sortedArray[curIdx-1]
            curIdx -= 1
        }
        sortedArray[curIdx] = temp
    }
    return sortedArray
}

// Generic
func insertionSort<T>(_ array: [T], _ isOrderedBefore: (T,T) -> Bool) -> [T] {
    var sortedArray = array
    for index in 1..<sortedArray.count {
        var curIdx = index
        let temp = sortedArray[curIdx]
        while curIdx > 0 && isOrderedBefore(temp, sortedArray[curIdx-1]) {
            sortedArray[curIdx] = sortedArray[curIdx-1]
            curIdx -= 1
        }
        sortedArray[curIdx] = temp
    }
    return sortedArray
}

let list = [10,-1,3,9,2,27,8,5,1,3,0,26]
print(insertionSort(list, <)) // [-1, 0, 1, 2, 3, 3, 5, 8, 9, 10, 26, 27]