# 정수론 - 골드바흐의 추측 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/9020
no_prime=[True for i in range(10002)]
no_prime[:1]=[False]*2

for i in range(2,int(10002/2)+1):
    if not no_prime[i]:continue
    j=2
    while i*j<=10001:
        no_prime[i*j]=False
        j+=1        


n=int(input())
for i in range(n):
    m=int(input())
    for j in range(int(m/2)):
        if no_prime[int(m/2)-j] and no_prime[m-(int(m/2)-j)]:
            print(int(m/2-j),int(m/2+j))
            break




