class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        num_question = len(questions)
        dp = [0]*num_question # dp[i] states how many point will I get if I choose question i

        def dfs(i):
            if i >= num_question:
                return 0
            if dp[i]:
                return dp[i]
            points, skip = questions[i]

            dp[i] = max(dfs(i + 1), points + dfs(i + skip + 1))
            return dp[i]
        
        return dfs(0)
      
questions = [[3,2],[4,3],[4,4],[2,5]]
obj = Solution()
obj.mostPoints(questions)
