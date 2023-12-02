class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_count = defaultdict(int)
        for ch in chars:
            char_count[ch]+=1
        
        ans = 0
        for word in words:
            word_count = defaultdict(int)
            for ch in word:
                word_count[ch]+=1
            
            good =True
            for ch, count in word_count.items():
                if char_count[ch]<count:
                    good = False
                    break
            
            if good:
                ans += len(word)
        
        return ans
