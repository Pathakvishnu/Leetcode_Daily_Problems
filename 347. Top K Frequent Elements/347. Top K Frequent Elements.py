class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for i in range(len(nums))]

        for num,freq in collections.Counter(nums).items():
            buckets[-freq].append(num)
        
        return list(itertools.chain(*buckets))[:k]
      
nums = [1,1,1,2,2,3]
k = 2

obj = Solution()
obj.topKFrequent(nums,k)
