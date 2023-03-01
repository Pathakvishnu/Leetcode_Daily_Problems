from typing import List

class Solution:
    def mergeSort(self,nums:List[int]) -> List[int]:
        if len(nums) > 1: 
            mid = len(nums)//2
            L = nums[:mid] 
            R = nums[mid:] 

            self.mergeSort(L)
            self.mergeSort(R)

            i = j = k = 0

            while i < len(L) and j < len(R): 
                if L[i] < R[j]: 
                    nums[k] = L[i] 
                    i+=1
                else: 
                    nums[k] = R[j] 
                    j+=1
                k+=1

            while i < len(L): 
                nums[k] = L[i] 
                i+=1
                k+=1

            while j < len(R): 
                nums[k] = R[j] 
                j+=1
                k+=1
            
    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergeSort(nums)
        return nums

nums = [5,1,1,2,0,0]
obj = Solution()
obj.sortArray(nums)
