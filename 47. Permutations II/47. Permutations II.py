class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        def backtrack(comb, freq):
            if len(comb)==n:
                ans.append(list(comb))
                return 

            for num in freq.keys():
                if freq[num]>0:
                    comb.append(num)
                    freq[num]-=1
                    backtrack(comb,freq)
                    comb.pop()
                    freq[num]+=1
            
        backtrack([],Counter(nums))

        return ans

inp = [1,2,3]
obj = Solution()
obj.permuteUnique(inp)
