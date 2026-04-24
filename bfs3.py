'''
N×M 크기의 격자안에 빙하의 정보가 주어집니다. 격자의 가장 바깥 부분은 항상 빙하가 아니고, 빙하를 제외한 나머지 위치에는 전부 물이 채워져 있습니다. 숫자 1은 빙하를, 숫자 0은 물을 나타냅니다.



빙하는 1초에 한 번씩 물에 닿아있는 부분들이 동시에 녹습니다. 하지만 빙하로 둘러싸여있는 물의 경우에는 붙어있는 빙하를 녹이지 못합니다. 여기서 닿아있다는 말은 상하좌우로 인접한 경우를 의미하며, 다음의 경우 역시 안쪽에 있는 0들은 빙하로 둘러쌓인 것이기 때문에 빙하가 녹는데 영향을 주지 못합니다.



맨 위에서 주어진 예시의 경우 안쪽에 있는 0은 빙하로 둘러싸여 있으므로 바깥쪽에 있는 0만이 빙하가 녹는데 영향을 미칩니다.



빙하가 전부 녹는데 걸리는 시간과 마지막으로 녹은 빙하의 크기(1의 개수)를 구하는 프로그램을 작성해보세요.

위의 예에서는 빙하가 녹는데 2초의 시간이 소요되며, 마지막으로는 크기가 4인 빙하가 녹으며 전부 없어지게 됩니다.

입력

제한 조건
출력

입력 예제
예제 1
입력

3 3
0 0 0
0 1 0
0 0 0
출력

1 1
예제 2
입력

6 7
0 0 0 0 0 0 0
0 1 1 1 1 0 0
0 1 1 0 1 1 0
0 1 0 1 1 1 0
0 1 1 1 1 1 0
0 0 0 0 0 0 0
출력

2 4
'''

from collections import deque

q=deque()
N, M = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(N)]
visited=[[False]*M for _ in range(N)]

# Please write your code here.
#빙하의 크기는 마지막 남은 1의 개수를 구하면 되고 
#녹이는 물인지 판단은 0 상하좌우에 1이 있으면 그건 못녹이는 물 / 나머지는 녹이는 물
#1을 보는데 bfs로 1을 다 찾아다니고 근데 그 1이 상하좌우에 0이 있어야 하고 
# 그 0이 하나라도 녹이는 물이면 ㄱㅊ
#근데 녹이지 못하는 물만 상하좌우중 하나면 그 빙하는 이번 시간에는 건들지 않기

#시간이 지나면 새로운 bfs로 들어가야함? 

#빙하 1개 검사할때 마다 / 상하좌우 번갈아가면서 물이 녹이는 물 혹은 녹이지 않는 물이지 판단하면됨



#아니면 0을 찾아서 bfs로 이어진 0보면서 0의 상하좌우에 1이 있는지보고
#상하좌우 전부에 1이 있다면 그 1은 건들지 않고 다음턴넘기고
#상하좌우 전부에 1이 없다면 그 1은 없애고0으로 만들기 
#없앤 1의 개수 그턴에 세어놓기
#그리고 없앤 1이후에 전체 좌표에 1이 없다면 그때 없앤 빙하 , 그리고 지금까지의 턴 뽑아놓기
dr=[-1,1,0,0]
dc=[0,0,-1,1]

def melt():
    q.append((0,0))
    visited=[[False]*M for _ in range(N)]
    visited[0][0]=True

    will_melt=[]

    while q:
        r,c=q.popleft()

        for i in range(4):
            nr=r+dr[i]
            nc=c+dc[i]

            if 0<=nr<N and 0<=nc<M and not visited[nr][nc]:
                visited[nr][nc]=True

                if a[nr][nc]==0:
                    q.append((nr,nc))
                elif a[nr][nc]==1:
                    will_melt.append((nr,nc))

    for r,c in will_melt:
        a[r][c]=0
    return len(will_melt)


time=0
last_melt=0

while True:
    melt_count=melt()

    if melt_count==0:
        break

    last_melt=melt_count
    time+=1
print(time, last_melt)




