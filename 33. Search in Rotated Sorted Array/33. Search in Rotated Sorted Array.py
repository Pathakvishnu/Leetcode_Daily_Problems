class Solution:
    """
    TC -> O(logn) + O(logn) --> to find the pivot index + to find the actual target
    """
    # main function 
    def search(self, nums: List[int], target: int) -> int:
        self.n = len(nums)
        pivot_idx = self.find_pivot(nums,0,self.n-1)
        if nums[pivot_idx]==target:
            return pivot_idx
        left_idx = self.binary_search(nums,0,pivot_idx-1,target)
        if left_idx!=-1:
            return left_idx
        rght_idx = self.binary_search(nums,pivot_idx+1,self.n-1,target)
        return rght_idx
      
    # binary search algo to find the pivot index
    def find_pivot(self,nums,start,end):
        while start<=end:
            if nums[start]<nums[end]:
                return start
            mid = start+(end-start)//2
            if nums[mid]<=nums[(mid+self.n-1)%self.n]:
                return mid
            elif nums[start]<=nums[mid]:
                start = mid+1
            else:
                end=mid-1
        return -1
      
    def binary_search(self,nums,start,end,target):
        while start<=end:
            mid = start+(end-start)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                end=mid-1
            else:
                start=mid+1
        return -1

nums = [4,5,6,7,0,1,2]
target = 0
        
