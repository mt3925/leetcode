# Design a data structure that follows the constraints of a Least Recently Used 
# (LRU) cache. 
# 
#  Implement the LRUCache class: 
# 
#  
#  LRUCache(int capacity) Initialize the LRU cache with positive size capacity. 
# 
#  int get(int key) Return the value of the key if the key exists, otherwise ret
# urn -1. 
#  void put(int key, int value) Update the value of the key if the key exists. O
# therwise, add the key-value pair to the cache. If the number of keys exceeds the
#  capacity from this operation, evict the least recently used key. 
#  
# 
#  Follow up: 
# Could you do get and put in O(1) time complexity? 
# 
#  
#  Example 1: 
# 
#  
# Input
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, null, -1, 3, 4]
# 
# Explanation
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // cache is {1=1}
# lRUCache.put(2, 2); // cache is {1=1, 2=2}
# lRUCache.get(1);    // return 1
# lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# lRUCache.get(2);    // returns -1 (not found)
# lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# lRUCache.get(1);    // return -1 (not found)
# lRUCache.get(3);    // return 3
# lRUCache.get(4);    // return 4
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= capacity <= 3000 
#  0 <= key <= 3000 
#  0 <= value <= 104 
#  At most 3 * 104 calls will be made to get and put. 
#  
#  Related Topics 设计 
#  👍 1218 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class ListNode:
    def __init__(self, key, value, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.node_map = {}
        self.count = 0

    def get(self, key: int) -> int:
        node = self.node_map.get(key)
        if not node:
            return -1

        node.prev.next = node.next
        node.next.prev = node.prev

        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node
        return node.value

    def put(self, key: int, value: int) -> None:
        if self.node_map.get(key):
            self.node_map[key].value = value
            self.get(key)
            return
        if self.count >= self.capacity:
            node = self.head.next
            del self.node_map[node.key]
            node.next.prev = node.prev
            node.prev.next = node.next
            del node
            self.count -= 1

        node = ListNode(key, value)
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node
        self.node_map[node.key] = node
        self.count += 1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# leetcode submit region end(Prohibit modification and deletion)
