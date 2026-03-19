# 재귀함수 - 하노이 탑 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/1914
def modify(a, b, c):

    a += 1

    b.append(4)

    c = [100, 200]


x = 10

y = [1, 2, 3]

z = [7, 8, 9]


modify(x, y, z)


print(x)  # (1)

print(y)  # (2)

print(z)  # (3)