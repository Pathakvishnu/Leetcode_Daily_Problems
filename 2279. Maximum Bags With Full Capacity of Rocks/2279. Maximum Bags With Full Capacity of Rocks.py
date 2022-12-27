from ast import List


class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        diff = list()
        ans = 0
        tot_sum = 0
        n = len(rocks)
        for i in range(n):
            temp_diff = capacity[i]-rocks[i]
            if temp_diff==0:
                ans+=1
            else:
                diff.append(temp_diff)
            tot_sum+=temp_diff
            # print(i,temp_diff,tot_sum)
        
        if tot_sum<=additionalRocks:
            # print("enter")
            return n
        diff = sorted(diff)
        # print(diff)
        idx = 0
        while additionalRocks:
            if additionalRocks>=diff[idx]:
                ans+=1
            else:
                break
            additionalRocks-=diff[idx]
            idx+=1
        return ans

capacity = [2,3,4,5]
rocks = [1,2,4,4]
additionalRocks = 2

obj = Solution()
print(obj.maximumBags(capacity,rocks,additionalRocks))