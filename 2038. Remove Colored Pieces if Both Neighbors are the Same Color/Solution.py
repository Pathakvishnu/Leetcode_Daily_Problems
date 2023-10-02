class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        alice=bob=0

        for i in range(1,len(colors)-1): # ignoring the edges
            if colors[i-1] == colors[i] == colors[i+1]:
                if colors[i]=='A':
                    alice+=1
                else:
                    bob+=1
            
        return alice>bob

colors = "AAABABB"
obj = winnerOfGame(colors)
