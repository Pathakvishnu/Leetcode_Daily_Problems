from ast import List


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        """
        1. Sort the nums since we want the sum
        2. Calculate the prefix sum
        3. For each query apply binary search in prefix sum array

        q = num of query
        n = number of element
        TC : O(qlogn) + O(n)
        SC : O(n)
        """
        nums = sorted(nums)
        n = len(nums)
        for i in range(1,n):
            nums[i] = nums[i]+nums[i-1]
        
        ans = []
        for q in queries:
            l=0
            r=n-1
            flag = False
            while l<=r:
                mid = (l+r)//2
                # print(f"l={l}r={r}mid={mid}")
                if nums[mid]==q:
                    print("enter")
                    ans.append(mid+1)
                    flag=True
                    break
                elif nums[mid]>q:
                    r = mid-1
                elif nums[mid]<q:
                    l = mid+1
            if not flag:
                ans.append(l)
        return ans