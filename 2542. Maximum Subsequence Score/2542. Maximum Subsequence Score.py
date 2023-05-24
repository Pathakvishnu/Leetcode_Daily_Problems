class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        group = [(a, b) for a, b in zip(nums1, nums2)]
        group.sort(key = lambda x: -x[1])
        
        top_k_heap = [x[0] for x in group[:k]]
        top_k_sum = sum(top_k_heap)
        heapq.heapify(top_k_heap)

        answer = top_k_sum * group[k - 1][1]

        for i in range(k, len(nums1)):
            top_k_sum -= heapq.heappop(top_k_heap)
            top_k_sum += group[i][0]
            heapq.heappush(top_k_heap, group[i][0])

            answer = max(answer, top_k_sum * group[i][1])
        
        return answer
      
nums1 = [1,3,3,2]
nums2 = [2,1,3,4]
k = 3

obj = Solution()
obj.maxScore(nums1,nums2,3)
