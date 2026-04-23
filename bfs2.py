'''
돌 잘 치우기


80XP

평균 180분

52% 정답률

총 제출 2,319회

숫자 0, 1로만 이루어진 N×N 격자가 주어졌습니다.

1이 돌을 나타낸다 할 때, 주어진 돌 중 M개의 돌만 적절하게 치워 K개의 시작점으로부터 상하좌우 인접한 곳으로만 이동하여 도달 가능한 칸의 수를 최대로 하는 프로그램을 작성해보세요.

숫자 0은 해당 칸이 이동할 수 있는 곳임을, 숫자 1은 돌이 있어 해당 칸이 이동할 수 없는 곳임을 의미합니다.

입력



제한 조건
출력

입력 예제
예제 1
입력

3 2 1
0 0 0
0 0 1
1 0 0
1 1
1 2
출력

8
예제 2
입력

4 2 2
0 1 1 0
0 1 1 0
0 1 1 1
0 1 0 0
1 4
4 4

출력

10



'''


from collections import deque
from itertools import combinations


n, k, m = map(int, input().split()) # m개의 돌을 치워야하고 k개의 시작점으로부터 도달가능한 칸수
# 0은 이동가능한 곳 1은 이동할 수 없는 곳
grid = [list(map(int, input().split())) for _ in range(n)]

start_points = []
for _ in range(k):
    r, c = map(int, input().split()) # 초기 시작위치
    start_points.append((r - 1, c - 1))

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


# Please write your code here.
#m개의 돌을 제거한 격자에서 출발시켜야 하는가 아니면-> 이거면 조합으로 2개 제거하고 들어가기->격자크기 100가능해서 
#계산수가 너무 많지 않을까? 
#bfs 돌리면서 m개의 돌을 제거하는 로직을 해야하는가 

#여긴 조합으로 m개의 돌 제거하는 로직
stones = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            stones.append((i, j))


def get_count(selected_stones):
    # 선택된 돌 제거
    for rs, cs in selected_stones:
        grid[rs][cs] = 0

    q = deque()
    visited = [[False] * n for _ in range(n)]
    count = 0

    # 멀티 소스 BFS: 시작점을 한꺼번에 큐에 삽입
    for sr, sc in start_points:
        if not visited[sr][sc]:
            visited[sr][sc] = True
            count += 1
            q.append((sr, sc))
    
    while q:
        curr_r, curr_c = q.popleft()

        for a in range(4):
            nr = curr_r + dr[a]
            nc = curr_c + dc[a]

            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and grid[nr][nc] == 0:
                visited[nr][nc] = True
                count += 1
                q.append((nr, nc))
    # 돌 원상복구
    for rs, cs in selected_stones:
        grid[rs][cs] = 1

    return count

max_total = 0
for selected_stones in combinations(stones, m):
    total = get_count(selected_stones)
    max_total = max(max_total, total)
print(max_total)






