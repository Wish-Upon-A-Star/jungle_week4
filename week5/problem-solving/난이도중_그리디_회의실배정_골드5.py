# 그리디 - 회의실 배정 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/1931
def select_meetings(meetings):
    if meetings==None:
        return 0
    meets = sorted(meetings, key=lambda x: x[1])
    selected = []
    for i in meets:
        if selected==[] or selected[-1][1]<i[0]:
            selected.append(i)
    return len(selected)

k=int(input())
meetings=[]
for _ in range(k):
    meetings.append(list(map(int,input().split())))

print(select_meetings(meetings))
