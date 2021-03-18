# Design and implement a data structure for a Least Frequently Used (LFU) cache.
#  
# 
#  Implement the LFUCache class: 
# 
#  
#  LFUCache(int capacity) Initializes the object with the capacity of the data s
# tructure. 
#  int get(int key) Gets the value of the key if the key exists in the cache. Ot
# herwise, returns -1. 
#  void put(int key, int value) Update the value of the key if present, or inser
# ts the key if not already present. When the cache reaches its capacity, it shoul
# d invalidate and remove the least frequently used key before inserting a new ite
# m. For this problem, when there is a tie (i.e., two or more keys with the same f
# requency), the least recently used key would be invalidated. 
#  
# 
#  To determine the least frequently used key, a use counter is maintained for e
# ach key in the cache. The key with the smallest use counter is the least frequen
# tly used key. 
# 
#  When a key is first inserted into the cache, its use counter is set to 1 (due
#  to the put operation). The use counter for a key in the cache is incremented ei
# ther a get or put operation is called on it. 
# 
#  
#  Example 1: 
# 
#  
# Input
# ["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "g
# et"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, 3, null, -1, 3, 4]
# 
# Explanation
# // cnt(x) = the use counter for key x
# // cache=[] will show the last used order for tiebreakers (leftmost element is
#   most recent)
# LFUCache lfu = new LFUCache(2);
# lfu.put(1, 1);   // cache=[1,_], cnt(1)=1
# lfu.put(2, 2);   // cache=[2,1], cnt(2)=1, cnt(1)=1
# lfu.get(1);      // return 1
#                  // cache=[1,2], cnt(2)=1, cnt(1)=2
# lfu.put(3, 3);   // 2 is the LFU key because cnt(2)=1 is the smallest, invalid
# ate 2.
#                  // cache=[3,1], cnt(3)=1, cnt(1)=2
# lfu.get(2);      // return -1 (not found)
# lfu.get(3);      // return 3
#                  // cache=[3,1], cnt(3)=2, cnt(1)=2
# lfu.put(4, 4);   // Both 1 and 3 have the same cnt, but 1 is LRU, invalidate 1
# .
#                  // cache=[4,3], cnt(4)=1, cnt(3)=2
# lfu.get(1);      // return -1 (not found)
# lfu.get(3);      // return 3
#                  // cache=[3,4], cnt(4)=1, cnt(3)=3
# lfu.get(4);      // return 4
#                  // cache=[3,4], cnt(4)=2, cnt(3)=3
#  
# 
#  
#  Constraints: 
# 
#  
#  0 <= capacity, key, value <= 104 
#  At most 105 calls will be made to get and put. 
#  
# 
#  
# Follow up: Could you do both operations in O(1) time complexity? Related Topic
# s 设计 
#  👍 344 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.freq_map = {}  # 访问次数 -> (该次数对应双向链表头、尾节点)
        self.node_map = {}  # key -> node
        self.count = 0
        self.min_freq = 0

    def get(self, key: int) -> int:
        if self.capacity <= 0:
            return -1
        node = self.node_map.get(key)
        if not node:
            return -1

        self.remove_node(node)
        self.add_node_freq(node)
        return node.value

    def remove_node(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next
        head, tail = self.freq_map.get(node.freq)
        if head.next == tail:
            del self.freq_map[node.freq]
            if self.min_freq == node.freq:
                self.min_freq = 0

    def add_node_freq(self, node):
        node.freq += 1
        head, tail = self.get_or_add_head_tail(node.freq)
        self.add_to_head(head, node)
        if not self.min_freq or self.min_freq > node.freq:
            self.min_freq = node.freq

    def get_or_add_head_tail(self, freq):
        rtn = self.freq_map.get(freq)
        if not rtn:
            head, tail = (ListNode(-1, -1), ListNode(-1, -1))
            head.next = tail
            tail.prev = head
            self.freq_map[freq] = (head, tail)
        else:
            head, tail = rtn
        return head, tail

    def add_to_head(self, head, node):
        node.next = head.next
        node.prev = head
        head.next.prev = node
        head.next = node

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return
        node = self.node_map.get(key)
        if node:
            node.value = value
            self.remove_node(node)
            self.add_node_freq(node)
            return

        if self.count >= self.capacity:
            _, tail = self.freq_map[self.min_freq]
            node = tail.prev
            self.remove_node(node)
            self.count -= 1
            del self.node_map[node.key]

        node = ListNode(key, value)
        self.node_map[key] = node
        self.add_node_freq(node)
        self.count += 1


class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
        self.freq = 0


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# leetcode submit region end(Prohibit modification and deletion)

# if __name__ == '__main__':
#     # obj = LFUCache(2)
#     # obj.put(1, 1)
#     # obj.put(2, 2)
#     # print(obj.get(1), )
#     # obj.put(3, 3)
#     # print(obj.get(2), )
#     # print(obj.get(3), )
#     # obj.put(4, 4)
#     # print(obj.get(1), )
#     # print(obj.get(3), )
#     # print(obj.get(4), )
#
#     import json
#     s = [[10],[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]]
#     r = json.loads('[null,null,null,null,null,null,-1,null,19,17,null,-1,null,null,null,-1,' \
#         'null,-1,5,-1,12,null,null,3,5,5,null,null,1,null,-1,null,30,5,30,' \
#         'null,null,null,-1,null,-1,24,null,null,18,null,null,null,null,14,' \
#         'null,null,18,null,null,11,null,null,null,null,null,18,null,null,-1,null,4,29,30,null,12,11,null,null,null,null,29,null,null,null,null,17,-1,18,null,null,null,-1,null,null,null,20,null,null,null,29,18,18,null,null,null,null,20,null,null,null,null,null,null,null]')
#     obj = LFUCache(s[0][0])
#     for item, r in zip(s[1:], r[1:]):
#         if len(item) == 2:
#             assert obj.put(*item) == r
#         else:
#             rst = obj.get(item[0])
#             print(item[0], r, rst)
#             assert rst == r
