class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        pop_idx = 0
        pop_len = len(popped)
        stack = []
        for ele in pushed:
            stack.append(ele)

            while stack and pop_idx<pop_len and stack[-1]==popped[pop_idx]:
                stack.pop()
                pop_idx+=1
            
        return pop_idx==pop_len
      
pushed = [1,2,3,4,5]
popped = [4,5,3,2,1]

