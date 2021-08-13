// Combination
func getCombination<T>(elements:[T], select: Int, repetition: Bool) -> [[T]] {
    func getCombination<T>(elements: ArraySlice<T>, select: Int, repetition: Bool,  partialResult: inout [T], totalResult: inout [[T]]) {
        guard select > 0 else {
            totalResult.append(partialResult)
            return
        }

        guard let firstElement = elements.first else { return }

        let remains = repetition ? elements : elements.dropFirst()

        partialResult.append(firstElement)
        getCombination(elements: remains, select: select-1, repetition: repetition, partialResult: &partialResult, totalResult: &totalResult)
        partialResult.removeLast()

        getCombination(elements: remains, select: select, repetition: repetition, partialResult: &partialResult, totalResult: &totalResult)
    }

    var result: [[T]] = []
    var partialResult: [T] = []

    getCombination(elements: elements[...], select: select, repetition: repetition, partialResult: &partialResult, totalResult: &result)

    return result
}

func combinations(_ array: [String]) -> Set<String> {
    if array.count == 0 { return [] }

    let answerArray = (0..<array.count).flatMap { i -> [String] in
        var removedArray = array
        let elem = removedArray.remove(at: i)
        return [elem] + combinations(removedArray).map { elem + $0 }
    }

    return Set(answerArray)
}