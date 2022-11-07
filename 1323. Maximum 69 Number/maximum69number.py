class Solution:
    def maximum69Number (self, num: int) -> int:
        num = str(num)
        for i,n in enumerate(num):
            if n=='6':
                return int(num[:i]+'9'+num[i+1:])
        
        return int(num)

num = 9969
obj = Solution()
print(obj.maximum69Number(num))