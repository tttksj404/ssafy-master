'''
초반에 storage를 999으로 두기
음식별로 식재료 2개씩 골라야함 
초반 음식은 일단 무작위로 식재료 2개 고르기 
골랐으면 
고른 식재료를 바탕으로 시너지 표에 있는 식재료별 좌표에 visited를 true로 바꿔주기

두번째 고를때 dfs로 visited 원복해줘야하지 않나? 그래야 처음부터 다시 고르지

이렇게 초반 음식은 확정된 상태로 

두번째 음식 식재료도 완전탐색하는데 visited false인 것만 고르고 두번째 음식과 첫번째 음식간 차이를 봤을때 최소가 되는걸 계속 갱신해주기

최소가 되었다면 해당 되는 최소 차이를 second_storage에 저장해두기 


storage랑 second를 비교해서 최솟값 갱신해주기 
나온 답은 이렇게 정하기 
1.각 음식에 들어갈 재료의 종류
->N개 중 N/2 개를 고르는 경우의 수(기저조건)
A음식에 절반재료
B음식에 절반재료
->재료의 종류(branch)

2.시너지 계산
A 음식 시너지 계산
B 음식 시너지 계산
->차이가 가장 작은 케이스 찾기
'''



def scores(ingredients, matrix):
    score=0
    size = len(ingredients)
    for i in range(size):
        for j in range(size):
            score +=matrix[ingredients[i]][ingredients[j]]
    return score

def dfs(idx,count):
    global min_diff

    if count==N//2:
        A=[]
        B=[]
        
        for i in range(N):
            if visited[i]:
                A.append(i)
            else:
                B.append(i)
        
        score_a = scores(A,ing)
        score_b = scores(B, ing)

        diff = abs(score_a-score_b)

        if diff < min_diff:
            min_diff= diff
        return
        
    for i in range(idx,N):
        if not visited[i]:
            visited[i]=True
            dfs(i+1,count+1)
            visited[i]=False

            if min_diff==0:
                return

T= int(input())
for tc in range(1,T+1):
    N=int(input())
    ing = [list(map(int, input().split())) for _ in range(N)]

    visited = [False]*N
    min_diff = 9999999999999

    visited[0]=True
    dfs(1,1)


    print(f'#{tc} {min_diff}')