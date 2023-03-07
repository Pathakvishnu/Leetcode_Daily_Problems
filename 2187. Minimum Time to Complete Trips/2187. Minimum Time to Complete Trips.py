from typing import List

class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        l,r = 1,max(time)*totalTrips

        def check_status(given_time):
            trips = 0
            for t in time:
                trips+=(given_time//t)
            
            return trips>=totalTrips

        while l<r:
            mid = (r-l)//2 + l
            if check_status(mid):
                r = mid
            else:
                l = mid+1

        return l
    
time = [1,2,3]
totalTrips = 5

obj = Solution()
obj.minimumTime(time,totalTrips)