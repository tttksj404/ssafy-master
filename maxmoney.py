'''
dfs 백트레킹? 
교환 횟수만큼 교환해놓고 계속 비교하고 비교했을때 최대값 안되면 백트레킹해놓기

가지치기 교환횟수 다채우고 나온값이 최대값보다 작으면 그냥 return

기저조건 교환횟수 다 채웠을때 
return


'''
T= int(input())
for tc in range(1,T+1):
    num, change =input().split()
    

