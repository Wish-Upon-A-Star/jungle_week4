# 백트래킹 - 외판원 순회 2 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/10971
n=int(input())

cities = []

for i in range(n):
    cities.append(list(map(int, input().split())))


def bitm(n,num):
    return ((2**n)&num)
def dfs(n,visit,now,city,val):

    if len(city[0])-1==n:
        #print(n,len(city[0]),city[now][0],val)
        if city[now][0]!=0:
            return val+cities[now][0]
    mins=2147483467
    for i in range(len(city[now])):
        if not bitm(i,visit)>0 and city[now][i]!=0:
            visit+=2**(i)
            temp=dfs(n+1,visit,i,city,val+city[now][i])
            visit-=2**(i)
            #print(temp,now,i)
            if temp<mins:
                #print(n,now,val,cities[now][0])
                mins=temp


            

    
    return mins
print(2**0)
val=dfs(0,1,0,cities,0)
print(val)