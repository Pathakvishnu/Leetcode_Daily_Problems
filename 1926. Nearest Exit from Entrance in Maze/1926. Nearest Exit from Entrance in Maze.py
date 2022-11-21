from typing import List


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        num_row,num_col = len(maze),len(maze[0])
        covered = set()
        covered.add((entrance[0],entrance[1])) # since we are standing there means its covered

        move = [(-1,0),(0,1),(1,0),(0,-1)]
        maze[entrance[0]][entrance[1]]="+"
        steps = 0
        while covered:
            new = set()
            for i,j in covered:
                for dx,dy in move:
                    x = i+dx
                    y = j+dy

                    if 0<=x<num_row and 0<=y<num_col and maze[x][y]=='.':
                        if (x==0 or x==num_row-1 or y==0 or y==num_col-1):
                            return steps + 1

                        if maze[x][y]==".":
                            new.add((x,y))
                            maze[x][y]="+"

            if new:
                steps+=1
            covered=new
        
        return -1

maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]]
entrance = [1,2]

obj = Solution()
print(obj.nearestExit(maze,entrance))
