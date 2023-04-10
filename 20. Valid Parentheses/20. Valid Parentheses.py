class Solution:
    def isValid(self, s: str) -> bool:

        stack = list()
        mapping = {')':'(','}':'{',']':'['}
        for char in s:
            if char in ['[','{','(']:
                stack.append(char)
            elif char in [']','}',')']:
                if not stack or mapping[char]!=stack.pop():
                    return False
            else:
                return False
        
        return stack==[]
 
s = "()[]{}"
obj = Solution()
obj.isValid(s)
