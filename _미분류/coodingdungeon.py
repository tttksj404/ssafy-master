'''
조건으로 걸려서 아닌 부분은 제거 해야하는 재귀 백트레킹 dfs 같음

1. 그래프에 시작노드 끝노드 필요한 골드 그래서 [a]=(b,c) 형태로 저장 대신 반대는 필요없음 어짜피 0에서 출발
2. 그냥 시작점 0이고 dfs 하기
3. 가지치기- 골드 c 가져오고 이걸 임의의 저장소에 더해주고  그럼 지금 지닌 골드 k의 값<임의의 저장소 되면 바로 쳐내기
4. 기저조건 - 그냥 가지치기에만 안걸리면 거기까지 그래서 딱히 필요없음
5. 조건 - 지금 추가되는 골드가 즉 임의의 저장소 속 골드가 K보다 작을땐 a의 값 따로 visited에 계속 넣어두기 
넣고 지금 임의의 저장소에 골드 추가한다음
그리고 dfs 돌리고 
visited에 a 다시 0으로 만들기(원복)

'''
def dfs(node, gold):
    

    if gold>K:
        return
    elif node!=0:
        ans.append(node)


    if visited[node]!=0:
        return
    
    
    else:
        visited[node]=1 #이거 반드시 해줘야함 위에 조건으로 작성해놨기 때문에 그리고 아래에서도 작성해놨음 1,0으로 구분짓는거 
        for next_node,next_gold in graph[node]:
            if visited[next_node]==0:
                if gold+next_gold<=K:
                    dfs(next_node,gold+next_gold)




        



T= int(input())
for tc in range(1,T+1):
    N,M,K= map(int, input().split())
    graph = [[] for _ in range(N+1)] # 그래프 만들때 한번 더 감싸는거 주의 
    visited= [0]*(N+1)
    ans=[]
    for _ in range(M):
        A,B,G=map(int,input().split())

        graph[A].append((B,G))
        graph[B].append((A,G))

    dfs(0,0)
    ans=sorted(list(set(ans)))
    print(f'#{tc}',*ans)







