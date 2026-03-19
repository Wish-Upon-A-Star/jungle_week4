# 스택 - 탑 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/2493
n=int(input())

a=[]
ans=[0]*(n+1)

array=list(map(int,input().split()))
a.append([array.pop(),n-1])

for i in range(len(array)-1,-1,-1):
    while a[len(a)-1][0]<array[i]:
        t,cur=a.pop()
        ans[cur]=i+1
        if a==[]:
            break
    if len(a)==0:
        a.append([array[i],i])
        continue

    if a[len(a)-1][0]>array[i]:
        a.append([array[i],i])
        continue       
        
for i in range(n):
    print(ans[i])
    



