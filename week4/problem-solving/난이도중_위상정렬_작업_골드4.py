# 위상정렬 - 작업 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2056
n=int(input())
ques=[]
times=[0]*(n+1)
degrees=[0]*(n+1)
premax=[0]*(n+1)
graph=[[]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    array=list(map(int,input().split()))
    times[i]=array[0]
    if array[1]==0:
        ques.append([0,i])
    else:
        for j in range(array[1]):
            degrees[i]+=1
            graph[array[2+j]].append(i)
    
maxt=0
while len(ques):
    now=ques[0]
    del ques[0]
    maxt=max(maxt,now[0]+times[now[1]])

    for i in graph[now[1]]:
        premax[i]=max(premax[i],now[0]+times[now[1]])
        degrees[i]-=1
        if degrees[i]==0:
            ques.append([premax[i],i])
print(maxt)