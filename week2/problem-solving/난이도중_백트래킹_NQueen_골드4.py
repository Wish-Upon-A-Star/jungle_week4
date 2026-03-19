# 백트래킹 - N-Queen (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/9663



def dfs(floor:int,n,answer,first_visi,d1,d2):
	if floor==n:
		answer+=1
	for i in range(n):
		if first_visi[i]==0 and d1[floor+i]==0 and d2[n-1-i+floor]==0:
			first_visi[i]=d1[floor+i]= d2[n-1-i+floor]=1
			answer=dfs(floor+1,n,answer,first_visi,d1,d2)
			first_visi[i]=d1[floor+i]= d2[n-1-i+floor]=0	
	return answer		
		
		

def main():
	first_visi=[0]*15
	d1=[0]*30
	d2=[0]*30
	n=int(input())
	ans2=dfs(0,n,0,first_visi,d1,d2)
	print("네?",ans2)
	
main()
