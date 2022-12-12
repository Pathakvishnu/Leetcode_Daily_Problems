class Solution:
    def simplifyPath(self, path: str) -> str:
        n = len(path)
        if path[-1]!='/':
            path=path+'/'
            n+=1

        stack = list()
        canonical_path = ""
        temp_path = ""

        idx = 1

        while idx<n:
            if path[idx]=='/':
                if temp_path=='' or temp_path=='.':
                    pass
                elif temp_path=='..':
                    if stack:
                        stack.pop()
                else:
                    stack.append(temp_path)
                temp_path=""
            else:
                temp_path+=path[idx]
            
            idx+=1

        canonical_path = "/"+"/".join(stack)
        if len(canonical_path)==0:
            canonical_path="/"
            
        return canonical_path

path = "/home//foo/"
obj = Solution()
print(obj.simplifyPath(path))