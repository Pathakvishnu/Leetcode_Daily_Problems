class Solution:
    def smallestSubsequence(self, s: str) -> str:
        occur = {}
        stack = []
        visited = set()

        for i,ch in enumerate(s):
            occur[ch] = i # keeping last occurence of each character
        
        for i,ch in enumerate(s):
            if ch not in visited:
                while stack and stack[-1]>ch and occur[stack[-1]]>i:
                    visited.remove(stack.pop())
                
                stack.append(ch)
                visited.add(ch)
            
        return ''.join(stack)
        
