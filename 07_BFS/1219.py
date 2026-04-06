"""
=============================================================
SWEA 1219 — 길찾기 (BFS/DFS)
=============================================================

[문제 풀면서 저질렀던 실수 정리]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. 방문 체크 (Visited) — 가장 치명적
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

(A) 백트래킹 오용
    X: visited[i][j] = False  ← 도달 여부만 묻는 문제에서 원복하면 TLE
    O: 도달/최단거리 문제 → 한번 방문하면 절대 안 품

(B) 체크 타이밍
    X: 큐에서 꺼낼 때 체크 → 같은 노드가 큐에 중복 삽입 → MLE
    O: 큐/스택에 넣기 직전에 visited[nr][nc] = True

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
2. 상태 공간 — 2D로 부족할 때
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

(A) 차원 누락
    X: visited[r][c] 만 씀 → 방향/메모리값 다르면 다른 상태인데 같은 상태로 처리
    O: 다음 행동을 결정짓는 모든 요소를 상태에 포함
       예: visited[r][c][direction][memory]

(B) 배열 선언 vs 접근 순서 불일치
    X: visited = [[0]*C for _ in range(R)]  →  visited[c][r] 로 접근 → IndexError
    O: for i in range(R): for j in range(C): → visited[i][j]
       선언 순서와 접근 순서 반드시 일치시키기

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
3. 탐색 루프 실수
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

(A) 기준 노드 혼동
    X: cur = q.popleft() 해놓고 → graph[start] 로 탐색 → 제자리걸음
    O: 반드시 방금 꺼낸 cur 기준으로 다음 노드 찾기

(B) 이동 후보군 무시
    X: next_dirs = [조건에 맞는 방향들] 만들어놓고 → for d in range(4) 로 전부 탐색
    O: for d in next_dirs 로만 돌기

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
4. 입력 / 배열 크기
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

(A) 노드 vs 간선 개수 착각
    X: N = 간선 개수 → graph = [[] for _ in range(N+1)] → 99번 노드에서 IndexError
    O: 노드 범위가 0~99면 상수 100으로 선언

(B) 파싱
    X: input().split() 만 → 붙어있는 숫자, 줄끝 공백 못 처리
    O: input().strip(), list(input()) 상황에 맞게

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
★ 문제 풀기 전 체크리스트 (3초 확인) ★
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

□ 배열 크기: 모르면 넉넉하게 (99번까지 → 100개)
□ 방문 체크: "갈 곳"에 미리 찍기 (visited[nr][nc] = True)
□ 상태 정의: 위치 + 방향 + 값 = 상태다 (4D visited)
□ 루프 기준: 큐에서 방금 꺼낸 놈의 친구를 찾기
□ 격자 워프: (i + dr) % R 으로 모듈러 처리
"""

# ── 풀이 (DFS, 스택) ──
for _ in range(10):
    tc, E = map(int, input().split())
    raw = list(map(int, input().split()))

    # 인접 리스트 — 노드 0~99 고정
    graph = [[] for _ in range(100)]
    for i in range(0, len(raw), 2):
        graph[raw[i]].append(raw[i + 1])

    # DFS
    stack = [0]
    visited = [False] * 100
    visited[0] = True
    result = 0

    while stack:
        cur = stack.pop()
        if cur == 99:
            result = 1
            break
        for nxt in graph[cur]:
            if not visited[nxt]:
                visited[nxt] = True  # 넣기 직전에 체크
                stack.append(nxt)

    print(f'#{tc} {result}')
