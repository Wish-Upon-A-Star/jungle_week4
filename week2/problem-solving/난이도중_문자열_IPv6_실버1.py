# 문자열 - IPv6 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/3107
ip = input().strip()

# :: 기준으로 나누기
if "::" in ip:
    left, right = ip.split("::")
    left = left.split(":") if left else []
    right = right.split(":") if right else []
    
    missing = 8 - (len(left) + len(right))
    mid = ["0000"] * missing
    
    parts = left + mid + right
else:
    parts = ip.split(":")

# 각 그룹을 4자리로 맞추기
for i in range(8):
    parts[i] = parts[i].zfill(4)

print(":".join(parts))