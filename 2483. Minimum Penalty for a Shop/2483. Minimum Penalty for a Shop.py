class Solution:
    def bestClosingTime(self, customers: str) -> int:
        # first count the 'Y' in the string 
        # reason being max penanlty in a given input is total number of 'Y'.
        current_penalty = min_penalty = customers.count('Y')

        # now start the iteration from 0th index
        # which implies when we close the shop at 0th hour the total penalty is the number of 'Y'
        min_hour_to_close = 0

        for idx, status in enumerate(customers):
            if status=='Y':
                current_penalty-=1
            else:
                current_penalty+=1
            
            if current_penalty<min_penalty:
                min_hour_to_close = idx+1
                min_penalty = current_penalty

        return min_hour_to_close
