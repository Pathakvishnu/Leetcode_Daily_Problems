class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1 = dict.fromkeys(nums1)
        nums2 = dict.fromkeys(nums2)

        res=[]
        for ele in nums1.keys():
            if nums2.get(ele,-1)==-1:
                temp.append(ele)
        
        res.append(temp)

        temp = []
        for ele in nums2.keys():
            if nums1.get(ele,-1)==-1:
                temp.append(ele)

        res.append(temp)

        return res

nums1 = [1,2,3]
nums2 = [2,4,6]

obj = Solution()
obj.findDifference(nums1,nums2)

