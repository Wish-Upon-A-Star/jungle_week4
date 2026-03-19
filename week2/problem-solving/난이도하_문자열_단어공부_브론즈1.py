# 문자열 - 단어 공부 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/1157   
str=input()

count=[0]*29
str=str.upper()
many=0
for i in str:
    count[ord(i)-65]+=1
    if many<count[ord(i)-65]:
        many=count[ord(i)-65]
    flag=''
for i in str:

    if flag=='' and many==count[ord(i)-65]:
        flag=i
        continue
    elif flag !=i and many==count[ord(i)-65]:
        flag="?"
        break
print(flag)