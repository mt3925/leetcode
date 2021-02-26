# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


subtree_set = set()
res = []


class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        res = []
        self.traverse(root, res, {})
        return res

    def traverse(self, root, res, subtree_map):
        if not root:
            return '#'

        left = self.traverse(root.left, res, subtree_map)
        right = self.traverse(root.right, res, subtree_map)

        subtree_str = ','.join([left, right, str(root.val)])
        subtree_map.setdefault(subtree_str, 0)
        subtree_map[subtree_str] += 1
        if subtree_map.get(subtree_str, 0) == 2:
            res.append(root)
        return subtree_str
