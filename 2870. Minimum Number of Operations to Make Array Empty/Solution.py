class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        if min(cnt.values()) == 1:
            return -1
        return sum(c // 3 + (c % 3 > 0) for c in cnt.values())     
