# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:

    def __init__(self, val=None, val_list=None):
        self.val = val
        self.val_list = val_list


    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """
        return self.val is not None

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """
        return self.val

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """
        return self.val_list


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = nestedList[::-1]

    def next(self) -> int:
        return self.stack.pop(-1).getInteger()

    def hasNext(self) -> bool:
        if not self.stack:
            return False
        if self.stack[-1].isInteger():
            return True
        self.stack.extend(self.stack.pop(-1).getList()[::-1])
        return self.hasNext()


# from leetcode Discuss
class NestedIterator(object):

    def __init__(self, nestedList):
        def gen(nestedList):
            for x in nestedList:
                if x.isInteger():
                    yield x.getInteger()
                else:
                    for y in gen(x.getList()):
                        yield y
        self.itr = gen(nestedList)
        self.latest = next(self.itr, None)

    def next(self) -> int:
        temp = self.latest
        self.latest = next(self.itr, None)
        return temp

    def hasNext(self) -> bool:
        return self.latest is not None


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())


if __name__ == '__main__':
    nestedList = [
            NestedInteger(val_list=[NestedInteger(1), NestedInteger(1)]),
            NestedInteger(2),
            NestedInteger(val_list=[NestedInteger(1), NestedInteger(1)]),
        ]
    i, v = NestedIterator(nestedList), []
    while i.hasNext():
        v.append(i.next())
    print(v)
