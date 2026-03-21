# 트리 - 트리 만들기 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/14244
n,m=list(map(int,input().split()))
print(0,1)
for i in range(2,m+1):
    print(1,i)
for j in range(m,n-1):
    print(j,j+1)
