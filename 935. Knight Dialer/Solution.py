class Solution:
    def knightDialer(self, n: int) -> int:
        if n==1 or n==2:
            return n*10
        @cache
        def num_sol(jumps_left,cell):
            if jumps_left==0:
                return 1
            tot = 0
            for next_cell in key_graph[cell]:
                tot = (tot + num_sol(jumps_left-1, next_cell)) % MOD
            
            return tot

        key_graph = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [3, 9, 0],
            5: [],
            6: [1, 7, 0],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4]
        }

        ans = 0
        MOD = 10**9+7
        for cell in range(10):
            ans = (ans + num_sol(n-1, cell)) % MOD
        
        return ans
