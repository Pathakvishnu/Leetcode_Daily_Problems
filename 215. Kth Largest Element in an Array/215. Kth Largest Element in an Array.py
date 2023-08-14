class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        ## modified counting sort algo (counter negative numbers)

        min_val,max_val = 1e5,-1e5
        for num in nums:
            if num>max_val:
                max_val = num
            if num<min_val:
                min_val = num

        count_arr = [0]*(max_val-min_val+1)
        for num in nums:
            count_arr[num-min_val]+=1
        
        remain = k
        for num in range(len(count_arr)-1,-1,-1):
            remain -=count_arr[num]
            if remain<=0:
                return num + min_val
        
        return -1
