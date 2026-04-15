'''
잡아야 하는 몬스터는 1잡으면 2->4까지 이렇게 잡는 순서로 가는데 몬스터 다 잡고 의뢰인 가도 괜찮고 몬스터 하나잡고 의뢰인 가도 괜찮음
bfs로 최단거리 구하면 되는데 아닌가? 
dfs로 재귀하면서 그다음 몬스터랑 의뢰인 변수 넣어두고 몬스터 안잡았는데 의뢰인 가는경우 가지치기해서 그냥 처리하는게 좋을듯

1.처음에 방문해야하는 몬스터랑 의뢰인 리스트 만들어놓기
2.dfs하는데 가지치기-> 해당 몬스터를 안들렸는데 의뢰인에게 가는 경우 
3.기저조건= 모든 리스트(몬스터, 의뢰인 다돌았을경우) 여기서 만약 전체 시간이 min보다 작으면 ok 아니면 return
4.다음 dfs는 간다음 백트레킹 구현하면됨 대신 왔던 경로에 백트레킹 하는게 아니고 방문할 리스트에서 visited 처리한걸 백트레킹하는거

'''

def dfs(si,sj,count,total_dist):
    global min_time

    if total_dist>=min_time:
            return
        
    if count==len(meetlist):
        if total_dist<min_time:
            min_time=total_dist
            return

    for i in range(len(meetlist)):
        if not havetomeet[i]:
            
            next=meetlist[i][2]


    



dr=[-1,1,0,0]
dc=[0,0,-1,1]

T= int(input())
for tc in range(1,T+1):
    N=int(input())
    village =[list(map(int,input().split())) for _ in range(N)]
    visited = [[False]*N for _ in range(N)]


    min_time=99999
    monster=0

    meetlist=[]
    for i in range(N):
        for j in range(N):
            if village[i][j]!=0:
                meetlist.append((i,j,village[i][j]))
                if village[i][j]>0:
                    monster+=1
    havetomeet=[False]*len(meetlist)
    monstercatch=[False]*5


    dfs(0,0,0,0)

    print(f'{tc} {min_time}')



'''

def dfs(now_r, now_c, total_dist, visited_count):
    global min_time

    # 가지치기: 이미 최솟값을 넘었으면 더 볼 필요 없음
    if total_dist >= min_time:
        return

    # 기저 조건: 모든 리스트(몬스터 + 의뢰인)를 다 돌았을 경우
    if visited_count == len(targets):
        min_time = min(min_time, total_dist)
        return

    # 방문할 리스트를 하나씩 확인
    for i in range(len(targets)):
        if not visited[i]:
            # [i][2] 이런 거 안 쓰고, 바로 꺼내서 이름표(r, c, val) 붙이기!
            target_r, target_c, val = targets[i]

            # 가지치기: 해당 몬스터를 안 들렀는데 의뢰인에게 가는 경우
            # val이 음수(의뢰인)일 때, 내 가방(bag)에 해당 번호가 없으면 패스
            if val < 0:
                monster_num = -val
                if monster_num not in bag:
                    continue

            # 방문 처리 (백트래킹 시작)
            visited[i] = True
            if val > 0: bag.add(val) # 몬스터면 가방에 넣기
            
            # 맨해튼 거리로 다음 지점까지 '점프' (BFS 대신 사용)
            dist = abs(now_r - target_r) + abs(now_c - target_c)
            
            dfs(target_r, target_c, total_dist + dist, visited_count + 1)

            # 백트래킹 원상복구
            if val > 0: bag.remove(val)
            visited[i] = False

# --- 메인 실행부 ---
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    village = [list(map(int, input().split())) for _ in range(N)]
    
    # 1. 방문해야 하는 몬스터랑 의뢰인 리스트 만들기
    targets = []
    for r in range(N):
        for c in range(N):
            if village[r][c] != 0:
                targets.append((r, c, village[r][c]))

    min_time = float('inf')
    visited = [False] * len(targets) # 리스트 방문 여부
    bag = set() # 현재 잡은 몬스터 번호 보관함

    # (0,0)에서 출발, 거리 0, 방문 0회
    dfs(0, 0, 0, 0)

    print(f'#{tc} {min_time}')
'''