class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles = sorted(piles,reverse=True)
        n = len(piles)
        ans = 0
        st = 1
        for i in range(n//3):
            ans+=piles[st]
            st+=2

        return ans
