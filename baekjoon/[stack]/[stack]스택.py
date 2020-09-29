# 스택 # B_10828

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


    def size(self):
        return self.count

    def _printList(self):
        node = self.head
        while node:
            print(node.value, end=" ")
            node = node.pointer
        print()


if __name__ == "__main__":
    stack = Stack()

    n = int(input())
    for i in range(n):
        ans = input().split()

        if ans[0]== "push":
            ans[1]=int(ans[1])
            stack.push(ans[1])
        if ans[0] == "top":
            print("{0}" .format(stack.peek()))
        if ans[0] == "size":
            print("{0}" .format(stack.size()))
        if ans[0] == "empty":
            if stack.isEmpty()==True:
                print('1')
            else:
                print('0')
        if ans[0] == "pop":
            print("{0}" .format(stack.pop()))
