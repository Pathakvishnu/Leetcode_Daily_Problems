class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # record = [0]*26
        # for alphabet in s:
        #     record[ord(alphabet)-ord('a')]+=1
        
        # for alphabet in t:
        #     record[ord(alphabet)-ord('a')]-=1
        #     if record[ord(alphabet)-ord('a')]<0:
        #         return alphabet

        record = defaultdict(int)
        for alphabet in s:
            record[alphabet]+=1
        
        for alphabet in t:
            record[alphabet]-=1
            if record[alphabet]<0:
                return alphabet
