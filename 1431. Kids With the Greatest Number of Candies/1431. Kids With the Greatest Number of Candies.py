class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_cand = max(candies)

        ans = []
        for kid_cand in candies:
            if kid_cand + extraCandies >= max_cand:
                ans.append(True)
            else:
                ans.append(False)
        
        return ans
      
  candies = [2,3,5,1,3]
  extraCandies = 3
  
  obj = Solution()
  obj.kidsWithCandies(candies,extraCandies)
