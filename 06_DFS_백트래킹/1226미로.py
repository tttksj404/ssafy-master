'''
최소로 도달없으므로 dfs

1.시작점 찾기 시작점은 2 끝점은 3
2. 가지치기- 그냥 목표에 도달하면 끝
3. 기저조건 - 목표에 도달하면 끝임

visited 하나만 챙기면됨
'''
dr=[-1,1,0,0]
dc=[0,0,-1,1]


def dfs(i,j):
    global flag

    if flag==True:  #flag로 가지치기해주기 문제에 명시적으로 적히지 않았더라도 자체적으로 가지치기 조건생각해보기
        return

    if maze[i][j]==3:
        flag=True
        return

    for a in range(4):
        nr=i+dr[a]
        nc=j+dc[a]

        if 0<=nr<100 and 0<=nc<100:
            if visited[nr][nc]==False:
                if maze[nr][nc]==0 or maze[nr][nc]==3:
                    visited[nr][nc]=True
                    dfs(nr,nc)
                    #visited[nr][nc]=False 여긴딱히 원복 필요없음 그냥 갈 수 있는지 없는지만 판단 
    




for tc in range(1,11):
    um=int(input())
    maze = [list(map(int,input().strip())) for _ in range(100)]
    visited = [[False]*100 for _ in range(100)]
    flag=False
    si,sj=0,0
    for i in range(100):
        for j in range(100):
            if maze[i][j]==2:
                visited[i][j]=True
                si,sj=i,j
    dfs(si,sj)
    
    if flag==False:
        print(f'#{tc} {0}')
    else:
        print(f'#{tc} {1}')

