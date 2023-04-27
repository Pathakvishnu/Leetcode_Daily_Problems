class Solution:
    def bulbSwitch(self, n: int) -> int:
        """
        Initially all bulbs are in off state, so only bulbs that are toogled odd number of times
        will remain on. So, we need to find those ith bulb which is a perfect square because only
        perfect square number has odd number of factors. 
        """
        # below code will give TLE 
        """
        count = 0
        for i in range(1,n+1):
            if (floor(sqrt(i))*floor(sqrt(i)))==i:
                count+=1
        return count
        """
        return int(sqrt(n))
      
n = 3
obj = Solution()
obj.bulbSwitch(n)
