class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        n = len(obstacles)
        answer = [1] * n
        
        # lis[i] records the lowest increasing sequence of length i + 1.
        lis = []
    
        for i, height in enumerate(obstacles):
            # Find the rightmost insertion position idx.
            idx = bisect.bisect_right(lis, height)
            
            if idx == len(lis):
                lis.append(height)
            else:
                lis[idx] = height
            answer[i] = idx + 1
            
        return answer
      
obstacles = [3,1,5,6,4,2]
obj = Solution()
obj.longestObstacleCourseAtEachPosition(obstacles)

