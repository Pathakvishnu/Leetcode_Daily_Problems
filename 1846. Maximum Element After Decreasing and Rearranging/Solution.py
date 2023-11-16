class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:

        # Solution 1
        arr = sorted(arr) #O(nlogn)

        if arr[0]!=1:
            arr[0] = 1
        max_ele = arr[0]
        for i in range(1,len(arr)):
            if abs(arr[i]-arr[i-1])<=1:
                pass
            else:
                arr[i] = arr[i-1] + 1

            if arr[i]>max_ele:
                max_ele = arr[i]
        
        return max_ele
