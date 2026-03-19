def exist(board: List[List[str]], word: str) -> bool:

    start=[]
    for i in range(len(board)):
        for j in range(len(board[i])):
            if word[0]==board[i][j]:
                start.append((i,j))

    for i in start:
        visit=[]
        sy,sx=i
        for j in range(len(board)):
            visit.append([0]*len(board[j]))
        visit[sy][sx]=1 
        bfs=[(sy,sx,0)]
        if len(word)==1:
            return True


        while len(bfs)>0:
            y,x,gi=bfs[0]
            print(bfs[0],board[y][x])
            bfs.pop(0)
            for u in range(-1,2):
                for lr in range(-1,2):
                    if u==0 and lr!=0 and lr+x>=0 and lr+x<len(board[0]):

                        
                        if word[gi+1]==board[y][lr+x] and visit[y][x+lr]==0:
                            if gi+1+1==len(word):
                                return True
                            
                            bfs.append((y,x+lr,gi+1))
                            visit[y][x+lr]=1

                    if u!=0 and lr==0 and u+y>=0 and u+y<len(board):
                        
                        if word[gi+1]==board[y+u][x] and visit[y+u][x]==0:
                            if gi+1+1==len(word):
                                return True
                            bfs.append((y+u,x,gi+1))
                            visit[y+u][x]=1

                        
    return False




    
            
print(-3/2,-3%2)