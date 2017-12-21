class ListNode(object):
    def __init__(self, v=None):
        self.value = v
        self.next = None
    
    def add_next(self, node):
        self.next = node
        return node


class Solution:
    def print_list_from_tail2head1(self, list_node):
        if not list_node:
            return
        self.print_list_from_tail2head1(list_node.next)
        print list_node.value,

    def print_list_from_tail2head2(self, list_node):
        if not list_node:
            return
        v_list = []
        p = list_node
        while p:
            v_list.insert(0, p.value)
            p = p.next
        for x in v_list:
            print x,


if __name__ == '__main__':
    l = ListNode(1)
    l.add_next(ListNode(2)).add_next(ListNode(5)).add_next(ListNode(33))
    Solution().print_list_from_tail2head1(l)
    Solution().print_list_from_tail2head2(l)
