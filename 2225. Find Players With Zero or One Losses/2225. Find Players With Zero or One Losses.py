import collections
from typing import List

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = [match[0] for match in matches]
        losers = [match[1] for match in matches]
        perfect_winners = list(set(winners) - set(losers))
        loser_counter = collections.Counter(losers)
        one_lost = []
        for loser in loser_counter:
            if loser_counter[loser] == 1:
                one_lost.append(loser)
        return [sorted(perfect_winners), sorted(one_lost)]
    
matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
obj = Solution()
obj.findWinners(matches)