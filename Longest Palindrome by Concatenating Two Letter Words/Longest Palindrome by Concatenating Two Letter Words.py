import collections
from typing import List

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        word_counter = collections.Counter(words) # O(n)
        
        length = 0
        center = False
        
        # O(n)
        for word,count in word_counter.items():
            
            if word[0]==word[1]:
                if count%2==0:
                    length+=count
                else:
                    length+=count-1
                    center=True
                    
            elif word[0]<word[1]:
                length += 2*min(count,word_counter[word[1]+word[0]])
        
        # to account for single word (with same letter) having odd occurence 
        if center:
            length+=1
            
        return 2*length
        
words = ["ab","ty","yt","lc","cl","ab"]
obj = Solution()
print(obj.longestPalindrome(words))