from ast import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        rgt = len(height)-1

        while left<rgt:
            max_area = max(max_area,((rgt-left)*min(height[left],height[rgt])))
            if height[left]<=height[rgt]:
                left+=1
            else:
                rgt-=1
        
        return max_area

height = [1,8,6,2,5,4,8,3,7]
obj = Solution()
print(obj.maxArea(height))