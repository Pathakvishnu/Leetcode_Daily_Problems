from collections import defaultdict


class TimeMap:
    """
    # we store information in the form of {key:{timestamp1:val,timestamp2:val...},key:{....}}
    # and also to make retrieval fast w.r.t each key we store it's latest timestamp
    """

    def __init__(self):
        self.store_key = defaultdict(dict) 
        self.max_time = defaultdict(int)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store_key[key][timestamp]=value
        self.max_time[key]=timestamp # store directly as we know timestamp is strictly increasing

    def get(self, key: str, timestamp: int) -> str:

        if self.store_key.get(key,0)==0:
            return ""
        if self.store_key[key].get(timestamp,0):
            return self.store_key[key][timestamp]
        
        if self.max_time[key]<=timestamp:
            return self.store_key[key][self.max_time[key]]

        key_info = None
        prev_t = 0
        for t,v in self.store_key[key].items():
            if t>timestamp:
                break
            if t<=timestamp and t>prev_t:
                key_info = v
        
        return key_info if key_info else ""
    


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)