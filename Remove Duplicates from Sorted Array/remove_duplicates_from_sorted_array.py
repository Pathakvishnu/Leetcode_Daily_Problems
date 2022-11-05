from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Using two pointers approach
        traverse_idx : traverse the given nums list
        insert_idx : keep track of index where to insert unqiue element
        curr_val : store recent unique element encountered

        return : insert_idx i.e till what index unqiue elements are present and sorted in nums list
        TC -> O(N)
        SC -> O(1)
        """
        curr_val = nums[0]
        insert_idx = 1
        traverse_idx = 1

        while traverse_idx<len(nums):
            if nums[traverse_idx]!=curr_val:
                nums[insert_idx] = nums[traverse_idx]
                curr_val = nums[traverse_idx]
                insert_idx+=1
            
            traverse_idx+=1
        
        return insert_idx

nums = [1,1,2,3,3,3,3,4]
obj = Solution()
print(obj.removeDuplicates(nums))