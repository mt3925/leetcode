# Definition for a binary tree node.
import collections


class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        result_list = []

        def _serialize(root):
            if root is None:
                result_list.append('None')
                return
            result_list.append(str(root.val))
            _serialize(root.left)
            _serialize(root.right)

        _serialize(root)
        return ','.join(result_list)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data_list = data.split(',')

        def _deserialize(data_list):
            if not data_list:
                return None
            val = data_list.pop(0)
            if val == 'None':
                return None
            root = TreeNode(val)
            root.left = _deserialize(data_list)
            root.right = _deserialize(data_list)
            return root

        return _deserialize(data_list)


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))


class Codec2:
    """层级遍历"""

    def serialize(self, root):
        if not root:
            return ''
        result_list = []
        q = collections.deque([root])
        while q:
            node = q.popleft()
            result_list.append(str(node.val) if node else '#')
            if node:
                q.append(node.left)
                q.append(node.right)
        while result_list[-1] == '#':
            result_list.pop()
        return ','.join(result_list)

    def deserialize(self, data):
        if not data:
            return None
        data_list = (int(i) if i != '#' else None for i in data.split(','))
        root = TreeNode(next(data_list))
        q = collections.deque([root])
        while q:
            node = q.popleft()
            lv = next(data_list, None)
            if lv is not None:
                node.left = TreeNode(lv)
                q.append(node.left)
            rv = next(data_list, None)
            if rv is not None:
                node.right = TreeNode(rv)
                q.append(node.right)
        return root


if __name__ == '__main__':
    bt = TreeNode(1, TreeNode(2, None, TreeNode(4)), TreeNode(3))
    data_str = Codec2().serialize(bt)
    print(data_str)
    print(Codec().serialize(bt))

    bt_new = Codec2().deserialize(data_str)
    print(Codec2().serialize(bt_new))
    print(Codec().serialize(bt_new))

    print(Codec2().serialize(Codec2().deserialize('')))
    print(Codec().serialize(Codec().deserialize('')))
    l = [4,-7,-3,None,None,-9,-3,9,-7,-4,None,6,None,-6,-6,None,None,0,6,5,None,9,None,None,-1,-4,None,None,None,-2]
    print(Codec2().serialize(Codec2().deserialize(','.join([str(i) if i is not None else '#' for i in l]))))
