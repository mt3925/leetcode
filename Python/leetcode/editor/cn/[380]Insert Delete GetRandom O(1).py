# Implement the RandomizedSet class: 
# 
#  
#  RandomizedSet() Initializes the RandomizedSet object. 
#  bool insert(int val) Inserts an item val into the set if not present. Returns
#  true if the item was not present, false otherwise. 
#  bool remove(int val) Removes an item val from the set if present. Returns tru
# e if the item was present, false otherwise. 
#  int getRandom() Returns a random element from the current set of elements (it
# 's guaranteed that at least one element exists when this method is called). Each
#  element must have the same probability of being returned. 
#  
# 
#  
#  Example 1: 
# 
#  
# Input
# ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert
# ", "getRandom"]
# [[], [1], [2], [2], [], [1], [2], []]
# Output
# [null, true, false, true, 2, true, false, 2]
# 
# Explanation
# RandomizedSet randomizedSet = new RandomizedSet();
# randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was insert
# ed successfully.
# randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
# randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contai
# ns [1,2].
# randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly
# .
# randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now cont
# ains [2].
# randomizedSet.insert(2); // 2 was already in the set, so return false.
# randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom
# () will always return 2.
#  
# 
#  
#  Constraints: 
# 
#  
#  -231 <= val <= 231 - 1 
#  At most 105 calls will be made to insert, remove, and getRandom. 
#  There will be at least one element in the data structure when getRandom is ca
# lled. 
#  
# 
#  
# Follow up: Could you implement the functions of the class with each function w
# orks in average O(1) time? Related Topics 设计 数组 哈希表 
#  👍 280 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import random


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data_list = []
        self.len = 0
        self.idx_map = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.idx_map:
            return False
        self.data_list.append(val)
        self.idx_map[val] = self.len
        self.len += 1
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        idx = self.idx_map.get(val)
        if idx is None:
            return False
        del self.idx_map[val]
        self.len -= 1
        if self.len != idx:
            self.data_list[idx] = self.data_list[self.len]
            self.idx_map[self.data_list[idx]] = idx
        self.data_list.pop()
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.data_list[random.randint(0, self.len - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# leetcode submit region end(Prohibit modification and deletion)
