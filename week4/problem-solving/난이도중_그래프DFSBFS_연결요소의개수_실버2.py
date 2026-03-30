# 그래프, DFS, BFS - 연결 요소의 개수 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/11724
import sys
input=sys.stdin.readline
n,m=list(map(int,input().split()))
graph=[[] for i in range(n+1)]
connect=[0]*(n+1)
for i in range(m):
    u,v=list(map(int,input().split()))
    graph[u].append(v)
    graph[v].append(u)


visit=[0]*(n+1)
ans=0

visits=n

for j in range(1,n+1):
    if visit[j]==0:
        ans+=1
        que=[j]
        visit[j]=1
        while len(que):
            now=que[0]
            del que[0]
            for i in graph[now]:
                if visit[i]==0:
                    visit[i]=1
                    que.append(i)

print(ans)