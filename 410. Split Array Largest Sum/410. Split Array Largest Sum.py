from ast import List

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def feasible(threshold) -> bool:
            count = 1
            total = 0
            for num in nums:
                total += num
                if total > threshold:
                    total = num
                    count += 1
                    if count > k:
                        return False
            return True

        left, right = max(nums), sum(nums)
        while left < right:
            mid = left + (right - left) // 2
            if feasible(mid):
                right = mid     
            else:
                left = mid + 1
        return left
    
nums = [7,2,5,10,8]
k = 2

obj = Solution()
print(obj.splitArray(nums,k))