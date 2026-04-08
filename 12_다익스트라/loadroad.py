import heapq

dr=[-1,1,0,0]
dc=[0,0,-1,1]

T=int(input())
for tc in range(1,T+1):
    N=int(input())
    graph = [list(map(int,input().strip())) for _ in range(N)]

    dist = [[float('inf')]*N for _ in range(N)]

    q=[]

    dist[0][0]=0
    heapq.heappush(q,(0,0,0))

    while q:
        cost,x,y=heapq.heappop(q)

        if cost>dist[x][y]:
            continue

        for i in range(4):
            nr= x+dr[i]
            nc= y+dc[i]

            if 0<=nr<N and 0<=nc<N:
                new_cost = cost+graph[nr][nc]

                if new_cost<dist[nr][nc]:
                    dist[nr][nc]=new_cost

                    heapq.heappush(q,(new_cost,nr,nc))

    print(f'#{tc} {dist[N-1][N-1]}')



