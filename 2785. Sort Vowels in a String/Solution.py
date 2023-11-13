class Solution:
    def sortVowels(self, s: str) -> str:

        vowel_count = {'a':0,'e':0,'i':0,'o':0,'u':0,'A':0,'E':0,'I':0,'O':0,'U':0}
        for char in s:
            if vowel_count.get(char,-1)!=-1:
                vowel_count[char]+=1

        ascii_sorted_vowel = 'AEIOUaeiou'
        ans = ''
        j = 0
        for i in range(len(s)):
            if vowel_count.get(s[i],-1)==-1:
                ans+=s[i]
            else:
                while vowel_count[ascii_sorted_vowel[j]]==0:
                    j+=1
            
                ans+=ascii_sorted_vowel[j]
                vowel_count[ascii_sorted_vowel[j]]-=1
            # print(vowel_count)

        return ans
