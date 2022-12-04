from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)

        if n2<n1:
            return self.findMedianSortedArrays(nums2,nums1)
        n = n1+n2
        low = 0
        high = n1

        while low<=high:
            cut1 = (low+high)//2
            cut2 = (n+1)//2 - cut1

            left1 = -1e9 if cut1==0 else nums1[cut1-1]
            left2 = -1e9 if cut2==0 else nums2[cut2-1]

            rgt1 = 1e9 if cut1==n1 else nums1[cut1]
            rgt2 = 1e9 if cut2==n2 else nums2[cut2]

            if left1<=rgt2 and left2<=rgt1:
                if n%2==0:
                    return (max(left1,left2)+min(rgt1,rgt2))/2
                else:
                    return max(left1,left2)
            
            elif left1>rgt2:
                high = cut1-1
            else:
                low = cut1+1
        return 0.0
        
nums1 = [1,2]
nums2 = [3,4]

obj = Solution()
print(obj.findMedianSortedArrays(nums1,nums2))
