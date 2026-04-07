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


'''
def scores(ingredients, matrix):
    score=0
    size = len(ingredients)
    for i in range(size):
        for j in range(size):
            score +=matrix[ingredients[i]][ingredients[j]]
    return score

def dfs(idx,count): #몇개를 선택했는지 count 
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
    '''

def cal_synergy(li):
    total = 0

    for i in range(len(li)):
        for j in range(i + 1, len(li)):
            a, b = li[i], li[j]
            total += arr[a][b] + arr[b][a]

    return total



def get_synergy():
    A_list, B_list = [], []
    # i 번째 재료의 visited 를 보고, 선택되었다면 A_list / 아니라면 B_list 에 추가
    for i in range(N):
        if visited[i]:
            A_list.append(i)
        else:
            B_list.append(i)

    return cal_synergy(A_list), cal_synergy(B_list)


# 재귀호출 -> N/2 개를 선택 (선택된 재료가 A 음식 / 선택 안된 재료가 B 음식)
def recur(cnt, prev):
    global min_answer

    if cnt == N // 2:
        # 시너지 계산
        a_total, b_total = get_synergy()
        min_answer = min(min_answer, abs(a_total - b_total))  # 최소값 갱신
        return

    for num in range(prev + 1, N):
        if visited[num]:
            continue

        visited[num] = 1
        recur(cnt + 1, num)
        visited[num] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * N
    min_answer = 21e8
    recur(0, 0)
    print(f"#{tc} {min_answer}")