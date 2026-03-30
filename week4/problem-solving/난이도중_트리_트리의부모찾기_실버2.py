# 트리 - 트리의 부모 찾기 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/11725
n=int(input())
array=[0]*(n+1)

graph = [[] for _ in range(n + 1)]
    
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

que=[1]
while len(que):
    now=que[0]
    del que[0]
    for i in graph[now]:
        if array[i]==0:
            que.append(i)
            array[i]=now


for i in range(2,len(array)):
    print(array[i])