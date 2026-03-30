n=int(input())
dp=[]
array=list(map(int,input().split()))
def binsearch(dp,n):
    high=len(dp)
    low=0
    while low<high:
        mid=(low+high)//2
        if dp[mid]>n:
            high=mid
        elif dp[mid]==n:
            return -1
        else:
            low=mid+1
    return low




for i in range(n):
    m=binsearch(dp,array[i])
    if len(dp)==m or len(dp)==0:
        dp.append(array[i])
    elif m==-1:
        continue
    else:
        dp[m]=array[i]

print(len(dp))
