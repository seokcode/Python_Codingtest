# 섬 연결하기

def solution(n, costs):
    answer = 0
    node = [i for i in range(n)]
    costs.sort(key=lambda x: x[2])

    def find(u):
        if u != node[u]:
            node[u] = find(node[u])
        return node[u]

    def union(u, v):
        root1 = find(u)
        root2 = find(v)
        node[root2] = root1

    for i in costs:
        if find(i[0]) != find(i[1]):
            union(i[0], i[1])
            answer += i[2]

    return answer