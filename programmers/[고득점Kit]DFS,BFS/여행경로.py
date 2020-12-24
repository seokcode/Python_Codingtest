# 여행경로(스택풀이)

def solution(tickets):
    tickets.sort(reverse=True)
    routes = dict()

    for p1, p2 in tickets:
        if p1 in routes:
            routes[p1].append(p2)
        else:
            routes[p1] = [p2]

    start = ["ICN"]
    answer = []
    while start:
        top = start[-1]
        if top not in routes or len(routes[top]) == 0:
            answer.append(start.pop())
        else:
            start.append(routes[top].pop())
    answer.reverse()
    return answer