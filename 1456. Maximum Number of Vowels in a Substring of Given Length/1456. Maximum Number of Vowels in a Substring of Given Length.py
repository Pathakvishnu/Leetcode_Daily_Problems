class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels_dict = {'a':1,'e':1,'i':1,'o':1,'u':1}
        n = len(s)
        max_vowel = 0
        for i in range(k):
            if vowels_dict.get(s[i],0):
                max_vowel+=1

        left = 1
        right = k

        vowel_count=max_vowel
        while right<n:
            if vowels_dict.get(s[left-1],0):
                vowel_count-=1
            if vowels_dict.get(s[right],0):
                vowel_count+=1

            max_vowel = max(vowel_count,max_vowel)
            left+=1
            right+=1

        return max_vowel
                
            
s = "abciiidef"
k = 3

obj = Solution()
obj.maxVowels(s,k)
