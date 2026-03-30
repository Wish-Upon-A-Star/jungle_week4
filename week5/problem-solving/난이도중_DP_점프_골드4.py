# DP - 점프 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2253
n,m=list(map(int,input().split()))
dp=[[0]*(152) for i in range(n+1)]
dp[2][1]=1
for _ in range(m):
    dp[int(input())][0]=-1
for i in range(2,n+1):
    if dp[i][0]==-1:
        continue
    for j in range(1,151):
        for k in range(-1,2):
            if j+k==0 or dp[i][j]==0:
                continue
            if i+j+k<=n:
                if dp[i+j+k][j+k]!=0:
                    dp[i+j+k][j+k]=min(dp[i][j]+1,dp[i+j+k][j+k])
                else:
                    dp[i+j+k][j+k]=dp[i][j]+1

maxi=n+2
for i in dp[n]:
    if i!=0:
        maxi=min(maxi,i)
if maxi==n+2:
    maxi= -1
print(maxi)
    
            

