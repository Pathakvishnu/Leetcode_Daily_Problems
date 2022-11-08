class Solution:
    def makeGood(self, s: str) -> str:
        stack = list()
        # n = len(s)
        for ch in s:
            if stack and stack[-1]==ch.swapcase(): 
                stack.pop(-1)
            else:
                stack.append(ch)
        return "".join(stack)

s = "leEeetcode"
obj = Solution()
print(obj.makeGood(s))