# 그리디 - 신입 사원 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/1946
n=int(input())
for _ in range(n):
    m=int(input())
    rank=[[0]*2 for _ in range(m)]
    for j in range(m):
        rank[j]=list(map(int,input().split()))
    rank = sorted(rank, key=lambda x: (x[0],x[1]))
    maxi=m+1
    ans=0
    for i in range(m):
        if rank[i][1]<maxi:
            ans+=1
            maxi=rank[i][1]

    print(ans)

