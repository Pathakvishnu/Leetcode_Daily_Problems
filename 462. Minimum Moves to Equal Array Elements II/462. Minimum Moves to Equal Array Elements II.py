from ast import List

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        """
        Since, we can increament and decrement any element in an array by 1 and we have to do it 
        in minimum moves.
        One, way to look at it is if we sort the array and find the middle idx of the sorted array
        and calculate every element distance to that middle element.It will give us min moves.

        Because, middle element will be at equal distance from both left and right sub array.
        """
        nums = sorted(nums)
        n = len(nums)
        middle = nums[n//2]

        return sum([abs(ele-middle) for ele in nums])

nums = [1,10,2,9]
obj = Solution()
print(obj.minMoves2(nums))