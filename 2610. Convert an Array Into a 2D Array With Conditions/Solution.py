class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        # approach 1
        freq = defaultdict(int)
        ans = []
        for num in nums:
            if len(ans)<=freq[num]:
                ans.append([])
            
            ans[freq[num]].append(num)
            freq[num]+=1
        return ans

        ## approach 2
        # count = Counter(nums)
        # k = max(count.values())
        # A = list(count.elements())
        # return [A[i::k] for i in range(k)]
