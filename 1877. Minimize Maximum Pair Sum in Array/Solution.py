class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        
        nums.sort()
        n = len(nums)
        low,high = 0,n-1
        max_pair_sum = 0

        while low<high:
            if max_pair_sum < (nums[low] + nums[high]):
                max_pair_sum = nums[low] + nums[high]

            low+=1
            high-=1

        return max_pair_sum
