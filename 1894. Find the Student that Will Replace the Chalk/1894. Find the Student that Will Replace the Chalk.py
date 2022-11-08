from typing import List

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total = sum(chalk)
        rem = k%total
        if rem==0:
            return 0
        for i in range(len(chalk)):
            if chalk[i]>rem:
                return i
            rem-=chalk[i]
            
chalk = [5,1,5]
k=22
obj = Solution()
print(obj.chalkReplacer(chalk,k))