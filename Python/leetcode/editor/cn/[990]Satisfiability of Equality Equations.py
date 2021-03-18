# Given an array equations of strings that represent relationships between varia
# bles, each string equations[i] has length 4 and takes one of two different forms
# : "a==b" or "a!=b". Here, a and b are lowercase letters (not necessarily differe
# nt) that represent one-letter variable names. 
# 
#  Return true if and only if it is possible to assign integers to variable name
# s so as to satisfy all the given equations. 
# 
#  
# 
#  
#  
# 
#  
#  Example 1: 
# 
#  
# Input: ["a==b","b!=a"]
# Output: false
# Explanation: If we assign say, a = 1 and b = 1, then the first equation is sat
# isfied, but not the second.  There is no way to assign the variables to satisfy 
# both equations.
#  
# 
#  
#  Example 2: 
# 
#  
# Input: ["b==a","a==b"]
# Output: true
# Explanation: We could assign a = 1 and b = 1 to satisfy both equations.
#  
# 
#  
#  Example 3: 
# 
#  
# Input: ["a==b","b==c","a==c"]
# Output: true
#  
# 
#  
#  Example 4: 
# 
#  
# Input: ["a==b","b!=c","c==a"]
# Output: false
#  
# 
#  
#  Example 5: 
# 
#  
# Input: ["c==c","b==d","x!=z"]
# Output: true
#  
# 
#  
# 
#  Note: 
# 
#  
#  1 <= equations.length <= 500 
#  equations[i].length == 4 
#  equations[i][0] and equations[i][3] are lowercase letters 
#  equations[i][1] is either '=' or '!' 
#  equations[i][2] is '=' 
#  
#  
#  
#  
#  
#  
#  Related Topics 并查集 图 
#  👍 155 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = UF(26)
        a_ord = ord('a')
        for item in equations:
            if item[1] == '=':
                uf.union(ord(item[0]) - a_ord, ord(item[3]) - a_ord)

        for item in equations:
            if item[1] == '!' and uf.connected(ord(item[0]) - a_ord, ord(item[3]) - a_ord):
                return False
        return True


class UF:
    def __init__(self, n):
        self.parents = list(range(n))
        self.sizes = [1 for _ in range(n)]
        self._count = n

    def union(self, p, q):
        root_p = self.get_root(p)
        root_q = self.get_root(q)
        if root_p == root_q:
            return

        if self.sizes[root_p] > self.sizes[root_q]:
            self.parents[root_q] = root_p
            self.sizes[root_p] += self.sizes[root_q]
        else:
            self.parents[root_p] = root_q
            self.sizes[root_q] += self.sizes[root_p]
        self._count -= 1

    def connected(self, p, q):
        return self.get_root(p) == self.get_root(q)

    def count(self):
        return self._count

    def get_root(self, x):
        while self.parents[x] != x:
            self.parents[x] = self.parents[self.parents[x]]
            x = self.parents[x]
        return x

# leetcode submit region end(Prohibit modification and deletion)
