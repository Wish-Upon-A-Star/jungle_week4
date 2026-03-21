# 트리 - 상근이의 여행 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/9372
t=int(input())
for i in range(t):
    n,m=list(map(int,input().split()))
    graph={}
    for j in range(n):
        graph[j]=[]
    for j in range(m):
        start,end=list(map(int,input().split()))
        
        graph[start-1].append(end-1)
        graph[end-1].append(start-1)
    visited=[0]*(n+1)
    que=[0]
    visited[0]=1
    while len(que)>0:
        now=que[0]
        del que[0]
        for k in graph[now]:
            if visited[k]==0:
                que.append(k)
                visited[k]=1
    ans=-1
    for j in visited:
        if j==1:
            ans+=1
    print(ans)


