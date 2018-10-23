class Node:
    def __init__(self, key= None, value = None):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None
        
class LRUCache:
    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.hash = {}
        self.head = Node(-1,-1) # dummy node
        self.tail = Node(-1, -1) # dummy node
        self.tail.prev = self.head
        self.head.next = self.tail
    """
    @param: key: An integer
    @return: An integer
    """
    def get(self, key):
        if key not in self.hash: return -1 
        node = self.hash[key]
        self.remove_node(node)
        self.move_to_tail(node)
        return node.val 
        
    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """
    def set(self, key, value):
        if self.get(key) != -1:
            self.hash[key].val = value
            return 
        if len(self.hash) >= self.capacity:
            self.pop_front()
        node = Node(key, value)
        self.move_to_tail(node)
        self.hash[key] = node
        
    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        
    def move_to_tail(self, node):
        node.prev = self.tail.prev 
        node.next = self.tail 
        node.prev.next = node 
        self.tail.prev = node
        
    def pop_front(self):
        del self.hash[self.head.next.key]
        self.head.next = self.head.next.next
        self.head.next.prev = self.head
