class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        min_speed = 1
        max_speed = 10e7
        ans_speed = -1

        def time_required(dist:List[int], speed: float):
            n = len(dist)
            total_time = 0
            for i in range(n):
                t =  dist[i]/speed
                if i==n-1:
                    total_time+=t
                elif dist[i]/speed!=dist[i]//speed:
                    total_time+=math.ceil(t)
                else:
                    total_time+=t
            return total_time

        while min_speed<=max_speed:
            mid = (min_speed+max_speed)//2
            if time_required(dist, mid)<=hour:
                ans_speed = mid
                max_speed = mid - 1
            else:
                min_speed = mid + 1

        return int(ans_speed)

dist = [1,3,2]
hour = 2.7

obj = Solution()
obj.minSpeedOnTime(dist,hour)
