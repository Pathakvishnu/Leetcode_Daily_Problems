from ast import List


class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        """
        let say removing index is repersented by k (0<k<n) 
        after removing an index k we split the array into two sub array i.e. left subarray and 
        right subarray.  
        left subarray where even and odd sum index doesn't change and hence sum won't change 
        right subarray where even index becomes odd index and vice versa

        For example :
        
        [2 1 6 4]
        left_arr = [0,0]
        rgt_arr = [8,5] # sum of even and odd indices

        After removing k=0
        rgt_arr even index i.e. 0 decrease by nums[k] so it becomes [6,4]
        left_arr remains same for now because we have remove index k=0 and there is no element
        before that. 

        After that we check if left_arr[0] + rgt_arr[1]==left_arr[1] + rgt_arr[0]

        So, question comes why did we do this?

        Answer is simple, if you remember I mentioned it left_arr indices doesn't change 
        whereas rgt_arr even indices becomes odd and vice versa. So, that's why I add
        left_arr[0]: representing even index sum with rgt_arr[1]: representing even index sum 
        after removal of index
        left_arr[1]: representing odd index sum with rgt_arr[0]: representing odd index sum 
        after removal of index

        After comparing if there sum is equal increase the counter by 1

        Then add removed index value to respective index in the left_arr.

        At starting left_arr = [0,0] but as you move to rgt rgt_arr tends to [0,0]
        """

        left_arr,rgt_arr = [0,0],[sum(nums[0::2]),sum(nums[1::2])]

        count = 0
        for k,ele in enumerate(nums):
            rgt_arr[k%2]-=ele
            if left_arr[0]+rgt_arr[1]==left_arr[1]+rgt_arr[0]:
                count+=1
            left_arr[k%2]+=ele
        
        return count


nums = [2,1,6,4]
obj = Solution()
print(obj.waysToMakeFair(nums))