# 해시 테이블 - 세 수의 합 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2295
n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

arr.sort()

two_sum = {}
for i in range(n):
    for j in range(i, n):
        two_sum[arr[i] + arr[j]] = True

answer = None
for d in range(n - 1, -1, -1):
    target = arr[d]
    for c in range(d + 1):
        need = target + (-arr[c])
        if two_sum.get(need):
            answer = target
            break
    if answer is not None:
        break

if answer is not None:
    print(answer)
