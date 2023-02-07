from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = dict()
        max_pick = 0

        l_idx = 0
        for r_idx in range(len(fruits)):
            basket[fruits[r_idx]] = basket.get(fruits[r_idx],0)+1

            while len(basket) > 2:
                basket[fruits[l_idx]] -= 1
                if basket[fruits[l_idx]] == 0:
                    del basket[fruits[l_idx]]
                l_idx += 1
            max_pick = max(max_pick, r_idx - l_idx + 1)
        
        return max_pick

fruits = [2,1,2,2,3,2,2]
obj = Solution()
obj.totalFruit(fruits)