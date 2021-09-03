import Foundation

func dfs(_ dict: inout [String:[String]],_ now: String, _ route: inout [String],_ N: Int) -> Bool {
    
    if let next = dict[now] {
        for (idx,d) in next.enumerated() {
            if d == "VISITED" { continue }
            
            route.append(d)
            dict[now]![idx] = "VISITED"
            
            if dfs(&dict, d, &route, N) { return true }
            
            route.popLast()
            dict[now]![idx] = d
        }
    }
    
    if route.count == N {
        return true
    }
    
    return false
}

func solution(_ tickets:[[String]]) -> [String] {
    let tickets = tickets.sorted { return $0[1] < $1[1] }
    var dict = [String:[String]]()
    var route = ["ICN"]
    
    for ticket in tickets {
        if let exist = dict[ticket[0]] {
            dict[ticket[0]] = exist+[ticket[1]]
        } else {
            dict[ticket[0]] = [ticket[1]]
        }
    }

    if dfs(&dict, "ICN", &route, tickets.count+1) {
        return route
    }
    
    return [String]()
}