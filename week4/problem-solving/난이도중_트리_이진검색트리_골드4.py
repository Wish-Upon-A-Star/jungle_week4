class TreeNode:
    def __init__(self, value):
        self.value = value
        self.parent = None

root = int(input())
last=root
result=[]
que=[]
x=1
while x!=60:
    try:
        #print(que)
        x = int(input())
        if len(que):
            for i in range(len(que)):
                target=que[i][1]
                quelor=que[i][2]
                if quelor=='L':
                    if target>x:
                        continue
                    for _ in range(i,len(que)):
                        result.append(que.pop()[0])
                    break
                if quelor=='R':
                    if target<x:
                        continue
                    for _ in range(i,len(que)):
                        result.append(que.pop())

                    break
            if len(que):

                lor="L" if x<que[-1][0] else "R"
                que.append([x,que[-1][0],lor])
            else:
                lor="L" if root>x else "R"
                que.append([x,root,lor])    

        else:
            lor="L" if root>x else "R"
            que.append([x,root,lor])


    except:
       break
#print("here",que,result)
while len(que):
    result.append(que.pop()[0])
result.append(root)

for i in result:
    print(i)