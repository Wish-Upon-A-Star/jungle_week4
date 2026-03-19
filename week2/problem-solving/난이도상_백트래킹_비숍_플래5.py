# 백트래킹 - 비숍 (백준 플래5)
# 문제 링크: https://www.acmicpc.net/problem/1799

maxx =maxxx=n=ans = 0
d1=[0]*30
d2=[0]*30
color1=[]
color2=[]
n=int(input())
for i in range(n):
    row = input().split()
    for j in range(n):
        color = int(row[j])
        if color == 1 and (i + j) % 2 == 0:
            color1.append((j, i))
        
        if color == 1 and (i+j)%2==1 :
            color2.append((j,i))
    
#dfs1(0)
#dfs2(0)
for i in color1:
    print(i)

print(maxx+maxxx)