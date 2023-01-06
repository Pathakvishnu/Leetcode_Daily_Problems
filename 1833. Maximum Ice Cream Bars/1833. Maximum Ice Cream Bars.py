from typing import List

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        """
        Counting sort
        """
        if coins>=sum(costs):
            return len(costs)

        max_ele = max(costs)
        count_arr = [0]*(max_ele+1)

        for ele in costs:
            count_arr[ele]+=1

        tot = 0
        for ele,count in enumerate(count_arr):
            if not count_arr[ele]:
                continue
            if coins<ele:
                break
            count = min(count_arr[ele], coins // ele)
            # We reduce price of picked ice creams from our coins.
            coins -= ele * count
            tot += count
             
        return tot

    # def maxIceCream(self, costs: List[int], coins: int) -> int:
    #     """
    #     Sorting
    #     """
    #     costs= sorted(costs) # python used tim sort alog which take extra O(n) space to do 
                               # in place sorting
    #     count = 0
    #     for ele in costs:
    #         if coins>=ele:
    #             count+=1
    #             coins-=ele
    #         else:
    #             break
    #     return count

costs = [1,3,2,4,1]
coins = 7
obj = Solution()
obj.maxIceCream(costs,coins)