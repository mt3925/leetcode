# There is a tree (i.e., a connected, undirected graph that has no cycles) consi
# sting of n nodes numbered from 0 to n - 1 and exactly n - 1 edges. Each node has
#  a value associated with it, and the root of the tree is node 0. 
# 
#  To represent this tree, you are given an integer array nums and a 2D array ed
# ges. Each nums[i] represents the ith node's value, and each edges[j] = [uj, vj] 
# represents an edge between nodes uj and vj in the tree. 
# 
#  Two values x and y are coprime if gcd(x, y) == 1 where gcd(x, y) is the great
# est common divisor of x and y. 
# 
#  An ancestor of a node i is any other node on the shortest path from node i to
#  the root. A node is not considered an ancestor of itself. 
# 
#  Return an array ans of size n, where ans[i] is the closest ancestor to node i
#  such that nums[i] and nums[ans[i]] are coprime, or -1 if there is no such ances
# tor. 
# 
#  
#  Example 1: 
# 
#  
# 
#  
# Input: nums = [2,3,3,2], edges = [[0,1],[1,2],[1,3]]
# Output: [-1,0,0,1]
# Explanation: In the above figure, each node's value is in parentheses.
# - Node 0 has no coprime ancestors.
# - Node 1 has only one ancestor, node 0. Their values are coprime (gcd(2,3) == 
# 1).
# - Node 2 has two ancestors, nodes 1 and 0. Node 1's value is not coprime (gcd(
# 3,3) == 3), but node 0's
#   value is (gcd(2,3) == 1), so node 0 is the closest valid ancestor.
# - Node 3 has two ancestors, nodes 1 and 0. It is coprime with node 1 (gcd(3,2)
#  == 1), so node 1 is its
#   closest valid ancestor.
#  
# 
#  Example 2: 
# 
#  
# 
#  
# Input: nums = [5,6,10,2,3,6,15], edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]]
# 
# Output: [-1,0,-1,0,0,0,-1]
#  
# 
#  
#  Constraints: 
# 
#  
#  nums.length == n 
#  1 <= nums[i] <= 50 
#  1 <= n <= 105 
#  edges.length == n - 1 
#  edges[j].length == 2 
#  0 <= uj, vj < n 
#  uj != vj 
#  
#  Related Topics 树 深度优先搜索 广度优先搜索 数学 
#  👍 7 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# from typing import List


class Solution:
    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        # 互质数字典
        coprime_map = {}
        for a in range(1, 51):
            for b in range(a, 51):
                if gcd(a, b) == 1:
                    coprime_map.setdefault(a, []).append(b)
                    coprime_map.setdefault(b, []).append(a)

        # 节点的边字典
        edge_map = {}
        for (x, y) in edges:
            edge_map.setdefault(x, []).append(y)
            edge_map.setdefault(y, []).append(x)

        # 祖先节点映射 值 ->（位置、深度）
        anc_val_pos_map = {}

        result_list = [-1] * len(nums)

        def dfs(idx, parent_idx, dep):
            val = nums[idx]

            result = (-1, -1)
            for c_v in coprime_map.get(val):
                anc_list = anc_val_pos_map.get(c_v, [])
                if anc_list and anc_list[-1][1] > result[1]:
                    result = anc_list[-1]
            result_list[idx] = result[0]

            anc_val_pos_map.setdefault(val, []).append((idx, dep))

            for neighbor in edge_map.get(idx, []):
                if neighbor == parent_idx:
                    continue
                dfs(neighbor, idx, dep+1)

            anc_val_pos_map.get(val, []).pop()
        dfs(0, -1, 0)
        return result_list


# def gcd(a, b):
#     if b == 0:
#         return a
#     if a == 0:
#         return b
#     return gcd(b, a % b)


# leetcode submit region end(Prohibit modification and deletion)

# if __name__ == '__main__':
#     # Input: nums = [5,6,10,2,3,6,15], edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]]
#     #
#     # Output: [-1,0,-1,0,0,0,-1]
#     # Input: nums = [2,3,3,2], edges = [[0,1],[1,2],[1,3]]
#     # Output: [-1,0,0,1]
#     print(Solution().getCoprimes([2,3,3,2], [[0,1],[1,2],[1,3]]))
#     print(Solution().getCoprimes([5,6,10,2,3,6,15], [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]]))


'''
class Solution {
    int[] ans;
    Map<Integer, List<Integer>> map = new HashMap<>(); // 边映射
    Map<Integer, List<Integer>> val = new HashMap<>(); // 互质数字典
    int[] dep;
    int[] pos = new int[52];
    public int[] getCoprimes(int[] nums, int[][] edges) {
        int n = nums.length;
        ans = new int[n];
        dep = new int[n];
        Arrays.fill(ans, - 1);
        Arrays.fill(pos, -1);

        for (int[] edge : edges) {
            int a = edge[0], b = edge[1];
            List<Integer> alist = map.getOrDefault(a, new ArrayList<>());
            alist.add(b);
            map.put(a, alist);
            List<Integer> blist = map.getOrDefault(b, new ArrayList<>());
            blist.add(a);
            map.put(b, blist);
        }

        for (int i = 1; i <= 50; i++) {
            for (int j = 1; j <= 50; j++) {
                if (gcd(i, j) == 1) {
                    List<Integer> list = val.getOrDefault(i, new ArrayList<>());
                    list.add(j);
                    val.put(i, list);
                }
            }
        }

        dfs(nums, 0, -1);
        return ans;
    }
    void dfs(int[] nums, int u, int form) {
        int t = nums[u];
        for (int v : val.get(t)) {
            if (pos[v] == -1) continue;
            if (ans[u] == -1 || dep[ans[u]] < dep[pos[v]]) ans[u] = pos[v];
        }
        int p = pos[t];
        pos[t] = u;

        for (int i : map.get(u)) {
            if (i == form) continue;
            dep[i] = dep[u] + 1;
            dfs(nums, i, u);
        }
        pos[t] = p;
    }
    int gcd(int a, int b) {
        if (b == 0) return a;
        if (a == 0) return b;
        return gcd(b, a % b);
    }
}
'''
