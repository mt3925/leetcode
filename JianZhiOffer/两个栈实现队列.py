
class Queue():
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        self.stack1.append(node)
    
    def pop(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if self.stack2:
            return self.stack2.pop()
        else:
            raise Exception("Queue is empty")


p = Queue()
p.push(10)
p.push(33)
p.push(2342)
print p.pop()
print p.pop()
p.push(232)
p.push(222)
print p.pop()
print p.pop()
print p.pop()
print p.pop()