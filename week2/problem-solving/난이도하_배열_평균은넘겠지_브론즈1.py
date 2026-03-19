# 배열 - 평균은 넘겠지 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/4344
n=int(input())
for i in range(n):
    m=list(map(int,(input().split())))
    eval=0
    for j in range(m[0]):
        eval+=m[j+1]
    eval/=m[0]
    count=0
    for j in range(m[0]):
        if eval<m[j+1]:
            count+=1
    print(f"{count/m[0]*100:.3f}"+"%")