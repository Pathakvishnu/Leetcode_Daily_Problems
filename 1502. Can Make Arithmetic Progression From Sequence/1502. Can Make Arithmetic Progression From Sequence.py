class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        min_val = min(arr)
        max_val = max(arr)

        n = len(arr)
        if (max_val - min_val)% (n-1):
            return False
        if max_val-min_val==0:
            return True
        
        diff = (max_val - min_val) // (n-1)
        
        check = set()
        for ele in arr:
            if (ele - min_val)%diff:
                return False
            check.add(ele)
        
        return len(check)==n

arr = [3,5,1]
