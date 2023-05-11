class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        """
        Similar to LCS(Longest Common Subsequence) Problem
        """
        n1 = len(nums1)
        n2 = len(nums2)

        dp = [[0]*(n2+1) for _ in range(n1+1)]

        for i in range(1,n1+1):
            for j in range(1,n2+1):
                if nums1[i-1]==nums2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])

        return dp[n1][n2]
   
nums1 = [2,5,1,2,5], nums2 = [10,5,2,1,5,2]
obj = Solution()
obj.maxUncrossedLines(nums1,nums2)


