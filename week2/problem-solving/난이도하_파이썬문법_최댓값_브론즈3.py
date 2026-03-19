# 파이썬 문법 - 최댓값 (백준 브론즈3)
# 문제 링크: https://www.acmicpc.net/problem/2562)
ints=[0]*9
for i in range(9):
    ints[i]=int(input())

ansi=0
max=-1
for i in range(len(ints)):
    if max<ints[i]:
        ansi=i+1
        max=ints[i]


print(ansi,max)

