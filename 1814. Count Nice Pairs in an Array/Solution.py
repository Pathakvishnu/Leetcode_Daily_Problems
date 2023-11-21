class Solution:
    def rev(self,num):
            result = 0
            while num:
                result = result * 10 + num % 10
                num //= 10
            
            return result
      
    def countNicePairs(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        for i in range(len(nums)):
            nums[i] = nums[i]-self.rev(nums[i])

        store = defaultdict(int)
        ans = 0

        for num in nums:
            ans = (ans + store[num]) % MOD
            store[num]+=1
        
        return ans

