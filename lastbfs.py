'''
우리는 하나


90XP

평균 180분

56% 정답률

총 제출 1,777회

N×N 크기의 격자로 이루어져 있는 나라의 정보가 주어집니다. 각 칸마다 하나의 도시가 있고, 각 도시마다의 높이 정보가 주어집니다. 이때 K개의 도시를 겹치지 않게 적절하게 골라, 골라진 K개의 도시로부터 갈 수 있는 서로 다른 도시의 수를 최대화 하고자 합니다. 이때 이동은 상하좌우로 인접한 도시간의 이동만 가능하며, 그 중에서도 두 도시간의 높이의 차가 U 이상 D 이하인 경우에만 가능합니다.

K개의 도시를 적절하게 골라 갈 수 있는 서로 다른 도시의 수를 최대로 하는 프로그램을 작성해보세요. (시작 도시를 포함하여 셉니다)

입력


제한 조건
출력

입력 예제
예제 1
입력

3 1 2 3
1 2 3 
2 4 5
2 1 5
출력

4
예제 2
입력

3 2 2 3
1 2 3
2 4 5
2 1 5
출력

6
예제 3
입력

3 1 2 3
1 3 5 
3 5 7
5 7 9
출력

9
'''
from collections import deque
from itertools import combinations

q=deque()
n, k, u, d = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]
# Please write your code here.
#u이상 d이하 인 두 도시간 높이의 차 만 가능함 
#k개 도시 고르고 각각 k에서 갈 수 있는 도시를 다 돌려서 그 도시와 k의 도시간 
#높이 차이가 u이상 d이하여야 후보 도시에 들어가있음 

#k개의 후보 도시 구해놓기
start_cities=[]
combs=combinations([(i,j) for i in range(n) for j in range(n)], k)
for comb in combs:
    start_cities.append(comb)


def bfs(start):
    q.append(start)
    visited[start[0]][start[1]]=True
    count=1

    while q:
        r, c = q.popleft()

        for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            nr, nc = r+dr, c+dc

            if 0<=nr<n and 0<=nc<n and not visited[nr][nc]:
                height_diff=abs(grid[r][c]-grid[nr][nc])
                if u<=height_diff<=d:
                    visited[nr][nc]=True
                    count+=1
                    q.append((nr,nc))
    return count
max_reachable=0
for cities in start_cities:
    visited = [[False]*n for _ in range(n)]
    total_reachable=0
    for city in cities:
        if not visited[city[0]][city[1]]:
            total_reachable+=bfs(city)
    max_reachable=max(max_reachable, total_reachable)

print(max_reachable)






