# 그래프, DFS, BFS - 점프왕 쩰리 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/16173
n=int(input())
maps = [[0] * n for _ in range(n)]
for i in range(n):
    maps[i]=list(map(int,input().split()))
visit=[[0]*n for _ in range(n)]
visit[0][0]=1
que=[]
que.append([0,0])
find=0

while len(que)>0:
    nowx,nowy=que[0]
    #print(nowx,nowy)
    
    if maps[nowy][nowx]==-1:
        find=1
        break
    del que[0]
    for x in [-1,0,1]:
        for y in [-1,0,1]:
            if (x+y)%2==1:
                
                movex=nowx+maps[nowy][nowx]*x
                movey=nowy+maps[nowy][nowx]*y

                if movex>=0 and movex<n and movey>=0 and movey<n and visit[movey][movex]!=1:

                    visit[movey][movex]=1
                    que.append([movex,movey])
if find:
    print("HaruHaru")
else:
    print("Hing")
