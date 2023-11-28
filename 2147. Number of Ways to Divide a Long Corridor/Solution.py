class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 10**9+7
        res = 1
        count_seat = 0
        start = 0
      
        for i in range(len(corridor)):
            if corridor[i]=='S':
                count_seat+=1

                if count_seat==2:
                    start = i
                elif count_seat==3:
                    res = (res*(i-start)) % MOD
                    count_seat=1
        
        if count_seat!=2:
            return 0

        return res
            
