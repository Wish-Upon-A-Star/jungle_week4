n=int(input())
dp=[[float('inf')]*(i+2) for i in range(n)]
array=[[] for _ in range(n)]
for i in range(n):
    array[i]=list(map(int,input().split()))
    dp[i][i]=0

for i in range(1,n):
    for j in range(1,i+1):
        for k in range(i-j,i+1):
            dp[i][i-j]=min(dp[i][i-j],dp[k][i-j]+dp[i][k+1]+array[i-j][0]*array[k][1]*array[i][1])



print(dp[n-1][0])
        
