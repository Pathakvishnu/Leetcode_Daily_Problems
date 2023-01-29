class ListNode:
    def __init__(self, key, value):
        """
        doubly linked list
        """
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.key_val = dict() # key to node
        self.capacity = capacity
        self.head = ListNode(0, 0)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.key_val:
            node = self.key_val[key]
            self.removeFromList(node)
            self.insertIntoHead(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if self.key_val.get(key,0):                   
            node = self.key_val[key]
            self.removeFromList(node)
            self.insertIntoHead(node)
            node.value = value       
        else: 
            if len(self.key_val) >= self.capacity:
                self.removeFromTail()
            node = ListNode(key,value)
            self.key_val[key] = node
            self.insertIntoHead(node)
			
    def removeFromList(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def insertIntoHead(self, node):
        headNext = self.head.next 
        self.head.next = node 
        node.prev = self.head 
        node.next = headNext 
        headNext.prev = node
    
    def removeFromTail(self):
        if len(self.key_val) == 0: return
        tail_node = self.tail.prev
        del self.key_val[tail_node.key]
        self.removeFromList(tail_node)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)