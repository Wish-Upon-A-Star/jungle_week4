class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans=0
        
        whatisland=[[[0] for i in range(len(grid[0]))] for j in range(len(grid))]
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):

                if grid[i][j]==1 :
                    if whatisland[i][j][0]==0:
                        ans+=1
                        whatisland[i][j][0]=ans
                    if j!=len(grid[i])-1 and grid[i][j+1]==1:
                        whatisland[i][j+1]=whatisland[i][j]
                    if i!=0 and grid[i-1][j]==1:
                        if whatisland[i-1][j]==0:
                            whatisland[i-1][j]=whatisland[i][j]
                        else:
                            #mins=min(whatisland[i-1][j][0],whatisland[i][j][0])
                            ans-=1
                            whatisland[i-1][j]=whatisland[i][j]

        return ans



                

                    



