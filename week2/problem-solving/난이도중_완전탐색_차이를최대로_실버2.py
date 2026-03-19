# 완전탐색 - 차이를 최대로 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/10819

n = int(input())
arr = list(map(int, input().split()))

used = [False] * n
perm = []
answer = 0

def dfs():
    global answer

    if len(perm) == n:
        total = 0
        for i in range(n - 1):
            total += abs(perm[i] - perm[i + 1])
        answer = max(answer, total)
        return

    for i in range(n):
        if not used[i]:
            used[i] = True
            perm.append(arr[i])

            dfs()

            perm.pop()
            used[i] = False


dfs()
print(answer)