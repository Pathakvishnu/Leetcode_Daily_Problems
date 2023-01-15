from heapq import heappush, heappop
from bisect import bisect, insort

def getInversion(A):
    n = len(A)
    if n<=1:
        return 0
    
    sortList = []
    result = 0

    for i,v in enumerate(A):
        heappush(sortList,(v,i))

    print(sortList)
    x = []
    while sortList:
        v,i = heappop(sortList)
        y = bisect(x,i)
        print(f"curr {x} pos {y}")
        result +=i-y
        insort(x,i)
        print(f"x={x}")
    
    return result

A = [1,20,6,4,5]
result = getInversion(A)
# print(result)