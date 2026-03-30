# DP - 평범한 배낭 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/12865
n,m=list(map(int,input().split()))

size=[0]*(m+1)
for i in range(n):
    j,k=list(map(int,input().split()))
    for l in range(m,-1,-1):
        if l==0:
            if j<=m:
                size[j]=max(size[j],k)        
        elif size[l]!=0:
            if l+j<=m:
                size[l+j]=max(size[l+j],size[l]+k)   

size.sort()
print(size[m])
