from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = list()
        n = len(temperatures)
        ans = [0]*n
        st_idx = n-1
        while st_idx>=0:
            if not stack:
                stack.append((temperatures[st_idx],st_idx))
            else:
                while stack:
                    if temperatures[st_idx]>=stack[-1][0]:
                        stack.pop()
                    else:
                        ans[st_idx] = stack[-1][1]-st_idx
                        stack.append((temperatures[st_idx],st_idx))
                        break
                if not stack:
                    stack.append((temperatures[st_idx],st_idx))
            # print(stack)
            st_idx-=1
        return ans

temp = [89,62,70,58,47,47,46,76,100,70]
obj = Solution()
print(obj.dailyTemperatures(temp))