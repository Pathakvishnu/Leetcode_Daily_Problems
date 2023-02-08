from ast import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        idx = n-2
        swap_i,swap_j = None,None
        while idx>=0:
            if nums[idx]<nums[idx+1]:
                swap_i = idx
                break
            idx-=1
        
        # you could right one reverse function because we are using it two times here
        # in the code
        if swap_i is None:
            l=0
            r = n-1
            while l<r:
                temp = nums[l]
                nums[l] = nums[r]
                nums[r] = temp
                l+=1
                r-=1
        
        else:
            idx = n-1
            while idx>=swap_i:
                if nums[idx]>nums[swap_i]:
                    swap_j = idx
                    break
                idx-=1

            temp = nums[swap_i]
            nums[swap_i] = nums[swap_j]
            nums[swap_j] = temp

            l=swap_i+1
            r = n-1
            while l<r:
                temp = nums[l]
                nums[l] = nums[r]
                nums[r] = temp
                l+=1
                r-=1


nums = [2,3,1]
obj = Solution()
obj.nextPermutation(nums)
        
