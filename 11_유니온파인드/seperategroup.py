def find(x):
    if parent[x]!=x:
        parent[x]=find(parent[x])
    return parent[x]

def union(a,b):
    rootA= find(a)
    rootB= find(b)
    if rootA!=rootB:
        parent[rootB]=rootA





T=int(input())


for tc in range(1,T+1):
    N,M = map(int,input().split()) #M쌍의 번호가 주어짐 

    pairs = list(map(int,input().split()))

    parent= list(range(N+1))

    for i in range(0,len(pairs),2):
        u,v = pairs[i], pairs[i+1]
        union(u,v)
    ans = 0
    for i in range(1,N+1):
        if parent[i]==i:
            ans+=1

    print(f'#{tc} {ans}')
