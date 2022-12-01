class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = {'a':1, 'e':1, 'i':1, 'o':1, 'u':1, 'A':1, 'E':1, 'I':1, 'O':1,'U':1}
        left = 0
        rgt = len(s)-1
        mid = left + (rgt-left)//2

        left_vow,rgt_vow = 0,0
        while left<=mid and rgt>=mid:
            if vowels.get(s[left],0):
                left_vow+=1
            if vowels.get(s[rgt],0):
                rgt_vow+=1
            left+=1
            rgt-=1
        
        if left_vow==rgt_vow:
            return True
        return False

s = "textbook"
obj = Solution()
print(obj.halvesAreAlike(s))