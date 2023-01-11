from ast import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        average_value = target // 4
        if average_value < nums[0] or nums[-1] < average_value:
                return res

        for i in range(n):
            if i==0 or nums[i-1]!=nums[i]:
                for j in range(i+1,n):
                    if j==i+1 or nums[j-1]!=nums[j]:
                        curr_target = target-(nums[i]+nums[j])
                        lo = j+1
                        hi = n-1

                        if nums[n-1]+nums[n-2]<curr_target:
                            continue

                        while lo<hi:
                            curr_sum = nums[lo]+nums[hi]
                            if curr_sum<curr_target or (lo>j+1 and nums[lo]==nums[lo-1]):
                                lo+=1
                            elif curr_sum > curr_target or (hi < n-1 and nums[hi] == nums[hi + 1]):
                                hi -= 1
                            else:
                                res.append([nums[i],nums[j], nums[lo], nums[hi]])
                                lo += 1
                                hi -= 1

        return res


nums = [1,0,-1,0,-2,2]
target = 0
obj = Solution()
obj.fourSum(nums,target)