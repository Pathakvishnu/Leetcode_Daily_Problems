class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:

        l = 0
        r = len(arr)

        while l<r:
            m = (l+r)//2
            if (arr[m-1]<arr[m]) and (arr[m]>arr[m+1]):
                return m
            elif arr[m-1]>arr[m]:
                r = m
            elif arr[m+1]>arr[m]:
                l = m

        return m

arr = [0,10,5,2]
obj = Solution()
obj.peakIndexInMountainArray(arr)
