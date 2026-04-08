import heapq

INF = int(1e9)

def dijkstra(start,N,graph):
    distance = [INF]*(N) #최단 신기록 적는 장부

    q=[] 
    heapq.heappush(q,(0,start)) 
    distance[start]=0

    while q:
        dist,now = heapq.heappop(q)

        if distance[now]<dist: #지금뽑은 dist가 장부보다 크면 과감히 버리기
            continue

        for neighbor,weight in graph[now]: #현재 노드와 연결된 다음 노드와 가중치 살피기
            cost = dist+weight #지금까지 비용은 거리랑 가중치 합친거

            if cost<distance[neighbor]: #만약 지금까지의 비용이 이미 장부에 적힌 비용보다 작으면 당연히 갱신
                distance[neighbor]=cost
                heapq.heappush(q,(cost,neighbor))

    return distance
    
    




T=int(input())
for tc in range(1,T+1):
    N,E=map(int,input().split())
    graph= [[] for _ in range(N+1)]
    for _ in range(E):
        a,b,w= map(int,input().split())
        graph[a].append((b,w))
    dist = dijkstra(0,N,graph) #
    target_dist= dist[N-1]

    if target_dist==INF:
        print(f'#{tc} impossible')
    else:
        print(f'#{tc} {target_dist}')



