class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        if numrows = 4
       P <-max_dist-> I    N 
       A <-max_dist-2*row -> L <-2*row -> S  I G ## row =1
       Y <-max_dist-2*row ->A <-2*row ->  H R ## row = 2
       P <-max_dist-> I

       So, first and last row will be formed from index at the jump of 2*(numRows-1)i.e. max_dist
       Rows in between will be formed from alternate index jump 
       first jump at max_dist-2*row
       second jump at 2*row, third jump at max_dist-2*row ... so on until length of string is ended
        
        """
        max_dist=numRows+(numRows-2)
        if max_dist==0:
            return s
        ans = ""
        for row in range(numRows):
            if row==0 or row==numRows-1:
                for ch_idx in range(row,len(s),max_dist):
                    ans+=s[ch_idx]
            else:
                jump = [max_dist-2*row,2*row]
                st_idx = row
                idx_to_pick = 0 # to alternate the pick index in jump
                while st_idx<len(s):
                    ans+=s[st_idx]
                    st_idx+=jump[idx_to_pick]
                    idx_to_pick=1-idx_to_pick
        
        return ans

s = "PAYPALISHIRING"
numRows = 4
obj = Solution()
obj.convert(s,numRows)