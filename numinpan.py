'''
일단 담을 수 있는 리스트에다가 동서남북 어떤 방향이든 6번만 이동하면 담아놓는 리스트 만들어놓고 
6자리 수는 하나로 묶어놓고 그걸 리스트에서 비교해서 set으로 총 리스트 개수세면됨

dfs로 처리해서 6번 하고

기저조건-> 6번 다하면 깃발 true true면 return

시작값에 따라서 시작되는 dfs로 생각

마지막에 visited false 초기화 시켜줘야함 
'''
def dfs(i,j,num):

    if len(num)==7:
        storage.add(num)
        return
    
    for a in range(4):
        nr = i+dr[a]
        nc= j + dc[a]

        if 0<=nr<4 and 0<=nc<4:
            dfs(nr,nc,num+str(pan[nr][nc]))
                

dr= [-1,1,0,0]
dc=[0,0,-1,1]

T= int(input())
for tc in range(1,T+1):
    pan = [list(map(int,input().split())) for _ in range(4)]
    storage=set()

    for i in range(4):
        for j in range(4):
            si,sj=i,j
            dfs(si,sj,str(pan[i][j]))

    print(f"#{tc} {len(storage)}")





