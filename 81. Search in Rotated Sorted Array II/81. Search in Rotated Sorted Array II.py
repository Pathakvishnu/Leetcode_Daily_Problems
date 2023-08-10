class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        nums_len = len(nums)
        if nums_len==1:
            if nums[0]!=target:
                return False
            else:
                return True

        left = 0
        right = nums_len-1

        while left<=right:
            while left<right and nums[left] == nums[left+1]:
                left+=1
            while left<right and nums[right] == nums[right-1]:
                right-=1
            mid = left + (right-left)//2

            if nums[mid]==target:
                return True

            elif nums[mid]>=nums[left]:
                if nums[mid]>=target and nums[left]<=target:
                    right = mid-1
                else:
                    left = mid+1
            
            else:
                if nums[mid]<=target and nums[right]>=target:
                    left=mid+1
                else:
                    right=mid-1

        return False

nums = [2,5,6,0,0,1,2]
target = 0
obj = Solution()
obj.search(nums,target)
