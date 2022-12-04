from typing import List


class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        if n==2:
            return skill[0]*skill[1]
        
        skill = sorted(skill)
        
        l = 0
        r = n-1
        
        count = skill[l] + skill[r]
        chemistry = 0
        while l<r:
            if (skill[l]+skill[r])!=count:
                return -1
            chemistry+=(skill[l]*skill[r])
            
            l+=1
            r-=1
            
        return chemistry
            
skill = [3,2,5,1,3,4]
obj = Solution()
print(obj.dividePlayers(skill))         
            