class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        """  sorting + iterating 
        TC -> O(nlogn) + O(n)
        SC -> O(1)
        Why didn't we sort with the first index let's say we sorted it with index 0
        then there is a possibility that the maximum number of all elements of the pair and minimum number of all aspects of the pair are actually forming a pair say (xm,ym).

        In that case, we can only form a chain of length 1 since ym is the largest of all and no element can be attached after that.
        """
        pairs = sorted(pairs,key=lambda k:k[1])
        curr = -1e4
        ans = 0
        for pair in pairs:
            if pair[0]>curr:
                ans+=1
                curr = pair[1]
        return ans

pairs_one = [[1,2],[2,3],[3,4]] 
pairs_two = [[-6,9],[1,6],[8,10],[-1,4],[-6,-2],[-9,8],[-5,3],[0,3]] # this case will fail when we sort it with index 0. Try it!!

obj = Solution()
obj.findLongestChain(pairs_two)
