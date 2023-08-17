class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        m,n = len(mat),len(mat[0])
        q = deque([])
        for i in range(m):
            for j in range(n):
                if mat[i][j]==0:
                    q.append((i,j))
                else:
                    mat[i][j]=-1

        while q:
            x,y = q.popleft()
            for i,j in (x-1,y),(x,y-1),(x+1,y),(x,y+1):
                if i<0 or i>=m or j<0 or j>=n or not mat[i][j]==-1:
                    continue

                mat[i][j] = mat[x][y] + 1
                q.append((i,j))

        return mat
