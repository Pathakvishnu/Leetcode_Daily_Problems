class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:

        # let us say each cell is a node and it's neighbour is (row+1,col) and (row,col+1) cells and we put the neighbours 
        # in queue so that we can store the result in the order we want

        queue = [(0,0)]
        ans = []
        while queue:
            row,col = queue.pop(0)
            ans.append(nums[row][col])

            if row+1 < len(nums) and col==0:
                queue.append((row+1,col))
            
            if col+1<len(nums[row]):
                queue.append((row,col+1))

        return ans
        
