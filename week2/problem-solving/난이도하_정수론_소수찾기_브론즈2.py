# 정수론 - 소수 찾기 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/1978
no_prime=[True for i in range(1002)]
no_prime[:1]=[False]*2

for i in range(2,int(1002/2)+1):
    if not no_prime[i]:continue
    j=2
    while i*j<=1000:
        no_prime[i*j]=False
        j+=1        


n=int(input())
nums=list(input().split())
count=0
for i in range(n):
    count+=no_prime[int(nums[i])]
for i in range(0,int(10)+1):print(i,no_prime[i])
print(count)