class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        ans = 0
        prefix_sum = 0

        """
        given index i lies between [1,n] and current index i will decrease by 1 and i-1
        index will increase by i+1. So, lets understand by taking n=2 as an example for better
        understanding and walk up for larger value of n

        n=2 nums=[5,10]
        since i>0 so we will take nums[1] which is 10
        if we decrease 10 by 1 and subsequently increase 5 by 1 -> [6,9] -> [7,8] -> [8,7] .. 
        so on until ith index become 0. 

        But as we can see, once we cross [7,8] or [8,7] maximum value of array will only increase
        so, we want one optimal point where maximum value of an array is minimized. And one can 
        think of average of both num ceil((8+7)/2) -> 8 (answer for above example)

        Now, lets take another example [7,8,4]...
        since we know considering subarray [7,8] our ans is 8 we move to next index i.e i=2
        andwe try solve for [8,4]. From above formula optimized value will be ceil((8+4)/2) = 6

        Answer of above array will be max([first subarray result, second subarray result]) i.e.
        max([8,6]) = 8. Now,question is why max? Now if you see if we 4 it's i-1 neigbour i.e. 8
        will only increase. If yo try to decrease the value 4 ---> 0 the previous index will 
        increase.

        """
        for i in range(len(nums)):
            prefix_sum += nums[i]
            ans = max(ans, math.ceil(prefix_sum / (i + 1)))

        return ans
      
obj = Solution()
nums = [3,7,1,6]
obj.minimizeArrayValue(nums)
