class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ## approach 1
        # device_arr = []
        # for num_str in bank:
        #     count=0
        #     for val in num_str:
        #         if val=='1':
        #             count+=1
        #     device_arr.append(count)
        
        # i = 0
        # j = i+1
        # tot = 0
        # while i<j and j<len(device_arr):
        #     if device_arr[j]==0:
        #         j+=1
        #         continue
        #     tot+=device_arr[i]*device_arr[j]
        #     i = j
        #     j+=1
        # return tot
        
        ## approach 2 (Space optimized)
        """
        Instead of using device_arr to store the count of 1 we can instead calculate the total device beam on the spot.
        """
        prev_dev = 0
        tot = 0
        for num_str in bank:
            curr_dev=0
            for val in num_str:
                if val=='1':
                    curr_dev+=1
            if curr_dev!=0:
                tot+=prev_dev*curr_dev
                prev_dev = curr_dev
        return tot
