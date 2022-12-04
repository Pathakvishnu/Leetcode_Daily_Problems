from typing import List


class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        free = 0
        wall = 1
        guard = 2
        seen = 3
        
        mat = [[free for _ in range(n)] for _ in range(m)]
        tot_cell = m*n
        g_cnt=0
        for g in guards:
            g_cnt+=1
            mat[g[0]][g[1]]=guard

        w_cnt= 0
        for w in walls:
            w_cnt+=1
            mat[w[0]][w[1]]=wall

        direction = [(-1,0),(1,0),(0,1),(0,-1)]
        for g in guards:
            for dx,dy in direction:
                x,y = g[0]+dx,g[1]+dy
                while (0 <= x < m) and (0 <= y < n):
                    if (mat[x][y] in [wall, guard]):
                        break
                    if (mat[x][y] != seen):
                        mat[x][y] = seen
                        tot_cell -= 1
                    x,y = x+dx,y+dy
        return tot_cell-w_cnt-g_cnt

m = 4
n = 6
guards = [[0,0],[1,1],[2,3]]
walls = [[0,1],[2,2],[1,4]]

obj = Solution()
print(obj.countUnguarded(m,n,guards,walls))