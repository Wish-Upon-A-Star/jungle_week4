class Solution:
    def simplifyPath(self, path: str) -> str:
        que=['/']
        dotstack=0
        name=''
        
        for i in range(len(path)-1):
            if path[i]=='/':
               if name=='.':
                   name=0
                   continue
               if name=='..':
                   if len(que)>1:
                    que.pop()
                    que.pop()
                   continue
               if name!='':
                   que.append(name)
                   que.append('/')
            else:
               name+=path[i]
                      
        name+=path[i]
        if path[i]=='/':
            if name=='.':
                name=0
            if name=='..':
                if len(que)>1:
                    que.pop()
                    que.pop()
            if name!='':
                que.append(name)
                que.append('/')
        if que[-1]=='/':
            que.pop()
        ret=''
        print(que)
        for i in que:
            ret+=i
        return ret
            

                