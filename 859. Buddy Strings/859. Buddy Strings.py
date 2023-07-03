859. Buddy Strings

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False
        
        if s==goal:
            char_count = [0]*26
            for ch in s:
                char_count[ord(ch)-ord('a')]+=1
                if char_count[ord(ch)-ord('a')]==2:
                    return True
            
            return False

        first_mismatch = -1
        second_mismatch = -1

        for i in range(len(s)):
            if s[i]!=goal[i]:
                if first_mismatch==-1:
                    first_mismatch = i
                elif second_mismatch==-1:
                    second_mismatch = i
                else:
                    return False

        if second_mismatch == -1: # that means we have only one mismatch index
            return False
        
        return s[first_mismatch]==goal[second_mismatch] and s[second_mismatch]==goal[first_mismatch]
