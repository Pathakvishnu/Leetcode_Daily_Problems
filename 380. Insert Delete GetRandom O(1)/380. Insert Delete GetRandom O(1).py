import random
"""
Problem Link : https://leetcode.com/problems/insert-delete-getrandom-o1/description/
"""
class RandomizedSet:

    def __init__(self):
        self.store_info = dict() # store data as key and there index as val
        self.val_lst = list() # store data 
        self.count=0 # maintain the counter for index updation

    def insert(self, val: int) -> bool:
        if self.store_info.get(val,-1)==-1:
            self.store_info[val] = self.count
            self.val_lst.append(val)
            self.count+=1
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        """
        When we remove a val from a randomized set we need to update the indexes of values occuring after that --> This makes no sense it increases the complexity
        
        So, to avoid that what we will do is pick last element from the randomized set and put it into the place of remove element and pop last element
        since it's placed somewhere else. 

        Benefit of second approach is now we don't have to spend time changing index values of elements.
        """
        if self.store_info.get(val,-1)==-1:
            return False
        else:
            last_val = self.val_lst[-1]
            indx = self.store_info[val]

            self.store_info[last_val]=indx
            self.val_lst[indx] = last_val

            self.store_info.pop(val)
            self.val_lst.pop()
            self.count-=1
            return True

    def getRandom(self) -> int:
        return random.choice(self.val_lst)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()