

def can_build(line, N, X):
    # 경사로 설치 여부를 기록
    visited = [False] * N
    
    for i in range(N - 1):
        # 높이가 같다면 통과
        if line[i] == line[i+1]:
            continue
        
        # 높이 차이가 1보다 크면 건설 불가
        if abs(line[i] - line[i+1]) > 1:
            return False
        
        # 1. 내리막 경사로 설치 (현재 > 다음)
        if line[i] > line[i+1]:
            target = line[i+1]
            # 앞쪽으로 X만큼의 공간이 있는지 확인
            for j in range(i + 1, i + 1 + X):
                if j >= N or line[j] != target or visited[j]:
                    return False
                visited[j] = True # 경사로 설치
                
        # 2. 오르막 경사로 설치 (현재 < 다음)
        elif line[i] < line[i+1]:
            target = line[i]
            # 뒤쪽으로 X만큼의 공간이 있는지 확인
            for j in range(i, i - X, -1):
                if j < 0 or line[j] != target or visited[j]:
                    return False
                visited[j] = True # 경사로 설치
                
    return True

def solve():
    T = int(input())
    for tc in range(1, T + 1):
        N, X = map(int, input().split())
        grid = [list(map(int, input().split())) for _ in range(N)]
        
        count = 0
        
        # 가로 방향 체크
        for r in range(N):
            if can_build(grid[r], N, X):
                count += 1
                
        # 세로 방향 체크
        for c in range(N):
            column_line = [grid[r][c] for r in range(N)]
            if can_build(column_line, N, X):
                count += 1
                
        print(f"#{tc} {count}")

solve()





#------------




#가로로직
# 한줄을 잡고 거기서 가장 큰 작은 수가 있는 걸 고른다음 오른쪽으로 x칸 만큼 계속 가다가 만약 수가 x칸 가기전에 커지면  out
# visted 처리해서 활주로 놓은거랑 탐색한부분은 visited 처리해놓기 한줄 볼때만 하면됨 한줄 다보면 그다음은 새로 visited 배열

#왼쪽으로도 살펴봐야함 끝에서부터 처음으로 오는로직
# visted 처리해서 활주로 놓은거랑 탐색한부분은 visited 처리해놓기 한줄 볼때만 하면됨 한줄 다보면 그다음은 새로 visited 배열

#세로로직
# 처음부터 아래로 내려가는 로직

# 끝에서 부터 올라오는 로직


    






