# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def binary_search(self,low,high,mountain_arr,condition,target=None):
        while low!=high:
            test_index = (low + high)//2
            if eval(condition):
                low = test_index+1
            else:
                high = test_index

        return low

    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        
        arr_length = mountain_arr.length()

        peak_index = self.binary_search(
            1,
            arr_length-2,mountain_arr,
           " mountain_arr.get(test_index) < mountain_arr.get(test_index + 1)")
        
        # search in increasing part of an array
        res = self.binary_search(
            0,
            peak_index,mountain_arr,
           " mountain_arr.get(test_index) < target", target)
        if mountain_arr.get(res) == target:
            return res

        # search in decreasing part of an array
        res = self.binary_search(
            peak_index+1,
            arr_length-1,mountain_arr,
           " mountain_arr.get(test_index) > target", target)
        if mountain_arr.get(res) == target:
            return res

        return -1
