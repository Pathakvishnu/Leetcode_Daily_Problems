from ast import List

class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        
        res = []
        ans = [0]*len(scores)
        for s,a in zip(scores,ages):
            res.append((a,s))   
    
        res = sorted(res,key=lambda k:(k[0],k[1]))
        best = 0
        for i in range(len(res)):
            ans[i] = res[i][1]
            for j in range(i):
                if res[i][1]>=res[j][1]:
                    ans[i] = max(ans[i],ans[j]+res[i][1])
            best = max(best,ans[i])
        
        return best

scores = [1,2,3,5]
ages = [8,9,10,1]

obj = Solution()
obj.bestTeamScore(scores,ages)
            