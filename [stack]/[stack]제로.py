# 제로 # B_10773
import sys

input=sys.stdin.readline

class Node(object):
    def __init__(self, value=None, pointer=None):
        self.value = value
        self.pointer = pointer


class Stack(object):
    def __init__(self):
        self.head = None
        self.count = 0

    def isEmpty(self):
        return not bool(self.head)

    def push(self, item):
        self.head = Node(item, self.head)
        self.count += 1

    def pop(self):
        if self.count==0:
            return -1
        elif self.count > 0 and self.head:
            node = self.head
            self.head = node.pointer
            self.count -= 1
            return node.value

    def peek(self):
        if self.count==0:
            return -1
        elif self.count > 0 and self.head:
            return self.head.value

    def _printList(self):
        node=self.head
        s=0
        while node:
            s+=node.value
            node=node.pointer
        print(s)


if __name__ == "__main__":
    stack = Stack()

    n = int(input())
    for i in range(n):
        ans = int(input())
        if ans==0:
            stack.pop()
        else:
            stack.push(ans)

    stack._printList()
