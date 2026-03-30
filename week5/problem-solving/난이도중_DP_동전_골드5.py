# DP - 동전 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/9084
n=int(input())

for _ in range(n):
    m=int(input())


    coins=list(map(int,input().split()))
    result=int(input())
    dp=[0]*(result+1)
    dp[0]=1
    for c in coins:
        for i in range(result+1):
            if dp[i]!=0:
                    if i+c<=result:
                        #print(i,c)
                        dp[i+c]+=dp[i]
    #print(dp)
    print(dp[result])
        
