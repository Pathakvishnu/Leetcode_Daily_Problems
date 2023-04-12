class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)
        n = len(people)-1
        boat = 0
        idx = 0
        while idx<=n:
            boat+=1
            if (people[idx] + people[n])<=limit:
                idx+=1
            n-=1
        return boat

people = [1,2]
limit = 3
obj = Solution()
obj.numRescueBoats(people,limit)
