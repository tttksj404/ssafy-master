'''
dfs
1. 메모리에 저장된 값 관리
2. 가지치기 조건 flag @이면 true 하고 true 면 맨위에서 return
3. 기저 조건 @면 true 하고 return 하기
4. ? -> 랜덤 함수
5. 벽으로 이동할시 맨처음 열로 이동하는 메커니즘 짜기 nr,  nc 조건 nr<0 nr>=N 일때 나눠서 명시 이때 방향이 같은쪽이면 마지막열 혹은 처음열로 이동




'''
#상하좌우
dr=[0,1,0,-1]
dc=[1,0,-1,0]


T= int(input())
for tc in range(1,T+1):
    R,C = map(int,input().split())
    commands = [input().strip() for _ in range(R)]
    visited = [[[[False for _ in range(16)] for _ in range(4)] for _ in range(C)] for _ in range(R)]

    #시작값은 0,0임
    stack=[(0,0,0,0)]
    visited[0][0][0][0]=True

    flag="NO"

    while stack:
        i,j,d,m=stack.pop()

        cmd=commands[i][j]
        next_dirs=[d]
        nm=m

        if cmd=="@":
            flag="YES"
            break
        elif cmd == '<': next_dirs = [2]
        elif cmd == '>': next_dirs = [0]
        elif cmd == '^': next_dirs = [3]
        elif cmd == 'v': next_dirs = [1]
        elif cmd == '_': next_dirs = [0 if m == 0 else 2]
        elif cmd == '|': next_dirs = [1 if m == 0 else 3]
        elif cmd == '?': next_dirs = [0, 1, 2, 3] # [핵심] 네 방향 다 가보기
        elif cmd == '+': nm = (m + 1) % 16
        elif cmd == '-': nm = (m - 1) % 16
        elif '0' <= cmd <= '9': nm = int(cmd)


        for nd in next_dirs:
            nr=(i+dr[nd])%R
            nc=(j+dc[nd])%C

            if not visited[nr][nc][nd][nm]:
                visited[nr][nc][nd][nm]=True
                stack.append((nr,nc,nd,nm))
 
    print(f'#{tc} {flag}')