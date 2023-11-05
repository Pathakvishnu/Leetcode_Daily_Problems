class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        max_ele = max(arr)
        n = len(arr)
        if k>=n:
            return max_ele

        curr = arr[0]
        winstreak = 0
        for i in range(1,n):
            opponent = arr[i]
            if curr>opponent:
                winstreak+=1
            else:
                curr = opponent
                winstreak=1
            
            if winstreak==k or curr==max_ele:
                return curr

arr = [2,1,3,5,4,6,7]
k = 2

obj = Solution()
obj.getWinner(arr,k)
