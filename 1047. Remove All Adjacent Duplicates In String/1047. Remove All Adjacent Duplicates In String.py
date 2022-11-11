class Solution:
    def removeDuplicates(self, inp: str) -> str:
        stack = list()
        for w in inp:
            if not stack:
                stack.append(w)
            else:
                top_ele = stack[-1]
                if top_ele==w:
                    pop_ele = stack.pop()
                else:
                    stack.append(w)
        return "".join(stack)

s = "abbaca"
obj = Solution()
print(obj.removeDuplicates(s))