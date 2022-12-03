class Solution:
    def frequencySort(self, s: str) -> str:
        freq_str = ""
        freq_dict = dict()

        for letter in s:
            freq_dict[letter] = freq_dict.get(letter,0) + 1
        
        sorted_freq_info = sorted(freq_dict.items(),key=lambda k:-k[1])
        for l,c in sorted_freq_info:
            freq_str+=l*c
        
        return freq_str

s = "Aabb"
obj = Solution()
print(obj.frequencySort(s))