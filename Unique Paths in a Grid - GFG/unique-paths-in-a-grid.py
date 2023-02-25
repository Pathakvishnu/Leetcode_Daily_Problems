#User function Template for python3

class Solution:
    def uniquePaths(self, n, m, grid):
        mod = 10**9+7
        paths = [[0]*m for _ in range(n)]
         
        if grid[0][0] == 1:
            paths[0][0] = 1

        for i in range(1, n):
            if grid[i][0] == 1:
                paths[i][0] = paths[i-1][0]
                 

        for j in range(1, m):
             
            if grid[0][j] == 1:
                paths[0][j] = paths[0][j-1]
                 
        for i in range(1, n):
            for j in range(1, m):
                if grid[i][j] == 1:
                    paths[i][j] = paths[i-1][j]+paths[i][j-1]
 
        return paths[-1][-1]%mod
        
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n,m=map(int,input().split())
        
        grid=[]
        for i in range(n):
            col = list(map(int,input().split()))
            grid.append(col)
        
        ob = Solution()
        print(ob.uniquePaths(n,m,grid))
# } Driver Code Ends