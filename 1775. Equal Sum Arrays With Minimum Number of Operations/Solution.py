class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        
        first_arr_sum, second_arr_sum = sum(nums1), sum(nums2)
        tot_diff = abs(first_arr_sum-second_arr_sum)
        if tot_diff==0:
            return 0
        min_operations = 0
        larger = nums1 if first_arr_sum>second_arr_sum else nums2
        smaller = nums1 if first_arr_sum<second_arr_sum else nums2

        heap = [(6-val)*-1 for val in smaller] + [(val-1)*-1 for val in larger]
        heapq.heapify(heap)
        while heap:
            val = heapq.heappop(heap)*-1
            tot_diff-=val
            min_operations+=1
            if tot_diff <= 0:
                return min_operations
        return -1
