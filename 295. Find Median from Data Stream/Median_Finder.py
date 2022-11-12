from heapq import heappop, heappush
"""
296. Best Meeting Point
More challenges
480. Sliding Window Median
1825. Finding MK Average
2102. Sequentially Ordinal Rank Tracker
"""

# with Binary Search
class MedianFinder:

    def __init__(self):
        self.size = 0
        self.data = list()

    # binary search to find the position where the next element will be inserted
    def findPos(self,ele):
        l = 0
        r = self.size-1
        while l<=r:
            mid = l+(r-l)//2
            if self.data[mid]<ele:
                l=mid+1
            else:
                r=mid-1
        return l

    # we keep on updating the array using binary search
    # although it's one drawback is in the inserting of the element which is really expensive operation.
    # to make it efficient we can also use binary search tree where insert operation is O(logN) where N is number of nodes

    def addNum(self, num: int) -> None:
        if self.size<1:
            self.data.append(num)
        else:
            pos = self.findPos(num)
            self.data.insert(pos,num) 
        self.size+=1
        # print(self.data)

    def findMedian(self) -> float:
        if self.size%2: # odd
            return self.data[self.size//2]
        else: # even
            return (self.data[self.size//2] + self.data[(self.size-1)//2])/2
        
# with min and max heap
class MedianFinder:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num: int) -> None:
        ### push num into the correct heap
        if not self.maxHeap or num <= -self.maxHeap[0]:
            heappush(self.maxHeap, -num)
        else:
            heappush(self.minHeap, num)
        
        ### banance the two heaps so that each of them representing half of the list
        ### for odd length list, len(maxHeap) == len(minHeap)+1
        ### for even length list, len(maxHeap) == len(minHeap)
        if len(self.minHeap) > len(self.maxHeap):
            heappush(self.maxHeap, -heappop(self.minHeap)) 
        elif len(self.maxHeap) > len(self.minHeap)+1:
            heappush(self.minHeap, -heappop(self.maxHeap)) 
        print(self.maxHeap)
        print(self.minHeap)

    def findMedian(self) -> float:

        if (len(self.maxHeap)+len(self.minHeap))%2==0:
            return (-self.maxHeap[0]+self.minHeap[0])/2
        return -self.maxHeap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
# [[], [1], [2], [], [3], []]
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()