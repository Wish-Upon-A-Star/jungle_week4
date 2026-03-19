# 링크드리스트 - 철도 공사 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/23309
import sys

prev_station = [-1] * 1000001
next_station = [-1] * 1000001

input = sys.stdin.readline
n, m = map(int, input().split())
stations = list(map(int, input().split()))

for i in range(n - 1):
    prev_station[stations[i]] = stations[i - 1]
    next_station[stations[i]] = stations[i + 1]

prev_station[stations[n - 1]] = stations[n - 2]
next_station[stations[n - 1]] = stations[0]

out = []
for i in range(m):
    inp = input().split()
    for j in range(len(inp)):
        if j != 0:
            inp[j] = int(inp[j])

    if inp[0] == 'BN':
        out.append(str(next_station[inp[1]]))
        prev_station[inp[2]] = inp[1]
        next_station[inp[2]] = next_station[inp[1]]
        prev_station[next_station[inp[1]]] = inp[2]
        next_station[inp[1]] = inp[2]

    elif inp[0] == 'BP':
        out.append(str(prev_station[inp[1]]))
        prev_station[inp[2]] = prev_station[inp[1]]
        next_station[inp[2]] = inp[1]
        next_station[prev_station[inp[1]]] = inp[2]
        prev_station[inp[1]] = inp[2]

    elif inp[0] == 'CN':
        out.append(str(next_station[inp[1]]))
        prev_station[next_station[inp[1]]] = inp[1]
        next_station[inp[1]] = next_station[next_station[inp[1]]]

    elif inp[0] == 'CP':
        out.append(str(prev_station[inp[1]]))
        next_station[prev_station[inp[1]]] = inp[1]
        prev_station[inp[1]] = prev_station[prev_station[inp[1]]]

sys.stdout.write("\n".join(out))
