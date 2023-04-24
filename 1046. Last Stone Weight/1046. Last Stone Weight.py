class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-1*ele for ele in stones]
        heapq.heapify(stones)

        n = len(stones)

        while n>1:
            a = -heappop(stones)
            b = -heappop(stones)

            if a==b:
                n-=2
            else:
                heappush(stones,-(a-b))
                n-=1

        return 0 if len(stones)==0 else -1*stones[0]

stones = [2,7,4,1,8,1]
obj = Solution()
obj.lastStoneWeight(stones)
