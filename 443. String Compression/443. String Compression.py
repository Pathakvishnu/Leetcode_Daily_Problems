from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        if n == 1:
            return 1
        
        left = 0
        right = 0
        
        while left < n:
            count = 1
            while left < n - 1 and chars[left] == chars[left+1]:
                count += 1
                left += 1
            
            chars[right] = chars[left]
            right += 1
            
            if count > 1:
                for c in str(count):
                    chars[right] = c
                    right += 1
            
            left += 1
        
        return right
    
chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
obj = Solution()
obj.compress(chars)