import heapq

INF= int(1e9)

def dijkstra(start,N,graph):
    distance = [INF]*(N+1)

    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0

    while q:
        dist,now = heapq.heappop(q)

        if distance[now]<dist:
            continue

        for neighbor, weight in graph[now]:
            cost = dist+ weight

            if cost<distance[neighbor]:
                distance[neighbor]=cost
                heapq.heappush(q,(cost,neighbor))

    return distance




T = int(input())
for tc in range(1,T+1):
    N,E = map(int,input().split()) #E 간선의 개수  N 노드의 개수
    graph = [[] for _ in range(N+1)]
    for _ in range(E):
        s,e,w = map(int,input().split())
        graph[s].append((e,w))

    dist_result = dijkstra(0,N,graph)
    
    print(f'#{tc} {dist_result[N]}')
