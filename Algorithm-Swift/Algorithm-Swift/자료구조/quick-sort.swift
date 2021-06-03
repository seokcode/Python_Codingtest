/*
[링크](https://github.com/raywenderlich/swift-algorithm-club/tree/master/Quicksort)
시간복잡도 최악: O(n^2)
최악의 경우: pivot value가 배열 내에서 가장 작은 값 or 가장 큰 값으로 정렬 되어있을 경우
매 partition마다 unbalanced partition이 이루어지고 그에따라 비교횟수가 늘어나서 O(n^2)이 된다.

시간복잡도 평균,최고: O(n log n)
*/

func quickSort<T: Comparable>(_ a: [T]) -> [T] {
    guard a.count > 1 else { return a }

    let pivot = a[a.count/2]
    let less = a.filter { $0 < pivot }
    let equal = a.filter { $0 == pivot }
    let greater = a.filter { $0 > pivot }

    return quickSort(less) + equal + quickSort(greater)
}

let list = [ 10, 0, 3, 9, 2, 14, 8, 27, 1, 5, 8, -1, 26 ]
print(quickSort(list)) // [-1, 0, 1, 2, 3, 5, 8, 8, 9, 10, 14, 26, 27]