class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        
        prefix_sum = [0]*(len(travel)+1)
        prefix_sum[0] = travel[0]
        for i in range(1,len(travel)):
            prefix_sum[i]=travel[i] + prefix_sum[i-1]

        last_pos = {'M':0,'P':0,'G':0}
        garb_count = {'M':0,'P':0,'G':0}
    
        for i in range(len(garbage)):
            for c in garbage[i]:
                last_pos[c] = i
                garb_count[c]+=1
        ans = 0
        for gar_type in last_pos.keys():
            if garb_count[gar_type]:
                ans+= garb_count[gar_type] + prefix_sum[last_pos[gar_type]-1]

        return ans
