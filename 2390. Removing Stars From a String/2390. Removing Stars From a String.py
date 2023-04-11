class Solution:
    def removeStars(self, s: str) -> str:
        record = list()
        for idx in range(len(s)):
            if s[idx]=="*":
                record.pop()
            else:
                record.append(s[idx])
        
        return "".join(record)
      
s = "leet**cod*e"
obj = Solution()
obj.removeStars(s)
