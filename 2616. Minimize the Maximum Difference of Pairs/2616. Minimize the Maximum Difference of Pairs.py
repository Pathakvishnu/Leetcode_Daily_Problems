class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums = sorted(nums)
        arr_len = len(nums)

        # find the valid pair
        def find_pair(threshold):
            idx, cnt = 0,0
            while idx < arr_len-1:
                if nums[idx+1]-nums[idx]<=threshold:
                    cnt+=1
                    idx+=1
                idx+=1
            return cnt

        low, high = 0, nums[-1]-nums[0]
        while low<high:
            mid = low + (high-low)//2

            if find_pair(mid)>=p:
                high = mid
            else:
                low = mid+1

        return low

nums = [10,1,2,7,1,3]
p = 2
