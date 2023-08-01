class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def backtrack(combination,next_idx,limit):
            if limit==0:
                ans.append(combination[:])
                return
            for next_i in range(next_idx,n+1):
                combination.append(next_i)
                backtrack(combination,next_i+1,limit-1)
                combination.pop()

        backtrack([],1,k)
        return ans

n = 4
k = 2

obj = Solution()
obj.combine(n,k)
