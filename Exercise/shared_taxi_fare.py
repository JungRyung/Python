import heapq

INF = int(1e9)

def dijstra(graph,distance,start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance

def solution(n, s, a, b, fares):

    graph = [[] for i in range( n + 1)]
    distanceS = [INF] * (n + 1)

    answer = 0

    for fare in fares:
        graph[fare[0]].append((fare[1],fare[2]))
        graph[fare[1]].append((fare[0],fare[2]))

    # s지점에서 시작하는 다익스트라알고리즘
    distanceS = dijstra(graph, distanceS, s)
    
    # p지점에서 시작하는 다익스트라알고리즘
    min = INF
    for p in range(1, n + 1):
        distanceP = [INF] * (n + 1)
        distanceP = dijstra(graph, distanceP, p)
        tmp = distanceS[p] + distanceP[a] + distanceP[b]
        if tmp < min:
            min = tmp
    answer = min
    return answer

n = 6
s = 4
a = 6
b = 2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]

answer = solution(n, s, a, b, fares)
print(answer)