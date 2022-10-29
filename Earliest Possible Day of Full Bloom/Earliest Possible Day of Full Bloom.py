from typing import List

class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        info = list(zip(plantTime,growTime))
        info = sorted(info,key=lambda k:k[1],reverse=True)
        tottime=0
        max_time=0
        for ptime,gtime in info:
            tottime+=ptime
            max_time = max(max_time, tottime+gtime)
            # print(tottime,max_time)
        return max_time

obj = Solution()
plantTime = [1,4,3]
growTime = [2,3,1]

print(obj.earliestFullBloom(plantTime,growTime))