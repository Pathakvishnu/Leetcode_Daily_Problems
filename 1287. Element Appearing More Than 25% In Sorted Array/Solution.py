class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        max_count = 0
        var_count = 1
        var = arr[0]
        ans = arr[0]
        for i in range(1,len(arr)):
            if arr[i]==var:
                var_count+=1
            else:
                if var_count>max_count:
                    ans = arr[i-1]
                    max_count = var_count
                var_count = 1
            var = arr[i]

        if var_count>max_count:
            ans = var
        return ans
                
