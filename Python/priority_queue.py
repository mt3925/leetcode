def parent(root):
    if root == 0:
        return 0
    return (root - 1) // 2


def left(root):
    return root * 2 + 1


def right(root):
    return root * 2 + 2


class MinPriorityQueue:
    """优先队列"""

    def __init__(self):
        self._data = []
        self.size = 0

    def swim(self, node_idx):
        parent_idx = parent(node_idx)
        if not parent_idx:
            return
        parent_v = self._data[parent_idx]
        node_v = self._data[node_idx]
        if parent_v <= node_v:
            return
        self._data[parent_idx], self._data[node_idx] = node_v, parent_v
        return self.swim(parent_idx)

    def sink(self, node_idx):
        left_idx = left(node_idx)
        right_idx = right(node_idx)
        if left_idx >= self.size:
            return
        compare_idx = left_idx
        compare_val = self._data[left_idx]
        if right_idx < self.size:
            right_val = self._data[right_idx]
            if right_val < compare_val:
                compare_idx = right_idx
                compare_val = right_val

        node_val = self._data[node_idx]
        if compare_val >= node_val:
            return
        self._data[node_idx], self._data[compare_idx] = compare_val, node_val
        return self.sink(compare_idx)

    def insert(self, value):
        self._data.append(value)
        self.swim(self.size)
        self.size += 1

    def del_min(self):
        if not self._data:
            return
        min_val = self._data[0]
        end_val = self._data.pop()
        if self._data:
            self._data[0] = end_val
        self.size -= 1
        self.sink(0)
        return min_val


class MaxPriorityQueue:
    """优先队列"""

    def __init__(self):
        self._data = []
        self.size = 0

    def swim(self, node_idx):
        parent_idx = parent(node_idx)
        if not parent_idx:
            return
        parent_v = self._data[parent_idx]
        node_v = self._data[node_idx]
        if parent_v >= node_v:
            return
        self._data[parent_idx], self._data[node_idx] = node_v, parent_v
        return self.swim(parent_idx)

    def sink(self, node_idx):
        left_idx = left(node_idx)
        right_idx = right(node_idx)
        if left_idx >= self.size:
            return
        compare_idx = left_idx
        compare_val = self._data[left_idx]
        if right_idx < self.size:
            right_val = self._data[right_idx]
            if right_val > compare_val:
                compare_idx = right_idx
                compare_val = right_val

        node_val = self._data[node_idx]
        if compare_val <= node_val:
            return
        self._data[node_idx], self._data[compare_idx] = compare_val, node_val
        return self.sink(compare_idx)

    def insert(self, value):
        self._data.append(value)
        self.swim(self.size)
        self.size += 1

    def del_max(self):
        if not self._data:
            return
        min_val = self._data[0]
        end_val = self._data.pop()
        if self._data:
            self._data[0] = end_val
        self.size -= 1
        self.sink(0)
        return min_val


if __name__ == '__main__':
    d = [1,3,5,2,4,2,4,7,12,5,3,62,4,6,2,3,7]
    mpq = MinPriorityQueue()
    for i in d:
        mpq.insert(i)
    r = []
    while mpq.size > 0:
        r.append(mpq.del_min())
    assert r == sorted(d)
