from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        curr_val = nums[0]
        insert_idx = 1
        traverse_idx = 1
        count=1
        while traverse_idx<len(nums):
            if nums[traverse_idx]==curr_val and count<=1 and count!=-1:
                nums[insert_idx] = nums[traverse_idx]
                insert_idx+=1
                count+=1
                if count==2:
                    count=-1

            if nums[traverse_idx]!=curr_val:
                nums[insert_idx] = nums[traverse_idx]
                curr_val = nums[traverse_idx]
                insert_idx+=1
                count=1

            traverse_idx+=1
        
        return insert_idx

nums = [1,1,1,2,2,3]
obj = Solution()
print(obj.removeDuplicates(nums))

